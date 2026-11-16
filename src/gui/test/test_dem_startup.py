import json
import time
from unittest.mock import Mock

import pytest
from builtin_interfaces.msg import Time
from std_msgs.msg import String

from gui.app import main_window
from gui.app.dem_planning_display import DemPlanningDisplay
from gui.app.dem_pure_pursuit import compute_command


def ros_side():
    node = Mock(
        _dem_pending_goal=None, _dem_request_id="", _dem_control_enabled=False,
        _dem_planning_ready=False, _dem_pending_control_config=None,
        _dem_control_config=None, _dem_local_path=[], _dem_odom_pose=None,
        _dem_odom_monotonic=0.0, _dem_last_goal_publish=0.0,
    )
    node.get_clock.return_value.now.return_value.to_msg.return_value = Time(sec=100)
    node.pub_dem_goal.get_subscription_count.return_value = 1
    return node


def test_goal_sent_before_planner_discovery_is_retried_with_same_request():
    node = ros_side()
    main_window.RosSide.send_dem_goal(node, 36.7, -4.48)
    goal = node._dem_pending_goal
    node._dem_last_goal_publish = time.monotonic() - 2
    main_window.RosSide._retry_dem_goal(node)
    assert node.pub_dem_goal.publish.call_args.args[0] is goal
    main_window.RosSide._on_dem_planning_status(
        node, String(data=json.dumps({"request_id": node._dem_request_id, "state": "WAITING_FOR_POSE"})),
    )
    assert node._dem_pending_goal is None
    count = node.pub_dem_goal.publish.call_count
    main_window.RosSide._retry_dem_goal(node)
    assert node.pub_dem_goal.publish.call_count == count


def test_execute_before_route_waits_then_starts_without_restarting_node():
    node = ros_side()
    cfg = {"v_forward": .5}
    assert not main_window.RosSide.start_dem_pure_pursuit(node, cfg)
    assert node._dem_pending_control_config == cfg
    node._dem_local_path = [(0.0, 0.0), (5.0, 0.0)]
    node._dem_odom_pose = (0.0, 0.0, 0.0)
    node._dem_odom_monotonic = time.monotonic()
    main_window.RosSide._retry_dem_goal(node)
    node.start_dem_pure_pursuit.assert_not_called()
    node._dem_planning_ready = True
    main_window.RosSide._retry_dem_goal(node)
    node.start_dem_pure_pursuit.assert_called_once_with(cfg)
    assert main_window.RosSide.start_dem_pure_pursuit(node, cfg)
    assert node._dem_pending_control_config is None


def test_manual_stop_cancels_queued_execution():
    node = ros_side()
    node._dem_pending_control_config = {"v_forward": .5}
    main_window.RosSide.stop_dem_pure_pursuit(node)
    assert node._dem_pending_control_config is None


def test_waiting_pose_and_arrival_have_explicit_display_states():
    display = DemPlanningDisplay()
    display.receive_state("WAITING_FOR_POSE")
    assert "calculando" in display.status()[0]
    display.receive_state("REACHED")
    assert "alcanzado" in display.status()[0]


@pytest.mark.parametrize("yaw", [0.0, 1.57, 3.14, -1.57])
def test_pure_pursuit_stops_at_one_meter_regardless_of_heading(yaw):
    assert compute_command([(0.0, 0.0), (5.0, 0.0)], (4.0, 0.0, yaw), 2, .5, .7) == (0, 0, True)
