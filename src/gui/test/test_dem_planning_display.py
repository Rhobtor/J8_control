from gui.app.dem_planning_display import DemPlanningDisplay


def test_empty_invalidation_does_not_replace_planning_status():
    display = DemPlanningDisplay()
    display.planning()
    display.receive_path(0)
    assert display.status() == ('DEM: calculando ruta…', '#8a5a00')


def test_path_and_ready_can_arrive_in_either_order():
    for path_first in (False, True):
        display = DemPlanningDisplay()
        display.planning()
        if path_first:
            display.receive_path(90)
            assert display.status()[0] == 'DEM: calculando ruta…'
            display.receive_state('READY')
        else:
            display.receive_state('READY')
            assert display.status()[0] == 'DEM: ruta lista'
            display.receive_path(90)
        assert display.status() == ('DEM: ruta 90 pts', '#187a37')


def test_empty_or_delayed_path_does_not_hide_failure():
    display = DemPlanningDisplay()
    display.receive_state('FAILED', 'No admissible approach')
    for point_count in (0, 90):
        display.receive_path(point_count)
        assert display.status() == ('DEM: sin ruta segura', '#b42318')
        assert display.error == 'No admissible approach'


def test_new_goal_resets_route_count_and_error():
    display = DemPlanningDisplay('FAILED', 90, 'Old failure')
    display.planning()
    assert display.point_count == 0
    assert display.error == ''
    display.receive_state('READY')
    assert display.status()[0] == 'DEM: ruta lista'
