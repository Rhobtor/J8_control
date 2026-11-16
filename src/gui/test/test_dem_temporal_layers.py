from unittest.mock import Mock

from nav_msgs.msg import OccupancyGrid

from gui.app import main_window


def test_local_grid_reaches_browser_with_separate_layer_name(monkeypatch):
    cells = [[1, 2, 100, 36.71, -4.48]]
    monkeypatch.setattr(main_window, '_positive_occupancy_cells_wgs84', lambda message: cells)
    node = Mock()
    message = OccupancyGrid()
    message.info.width = message.info.height = 5
    main_window.RosSide._on_dem_temporal_grid(node, 'local', message)
    node.dem_temporal_callback.assert_called_once_with(
        'local', {'width': 5, 'height': 5, 'cells': cells}
    )


def test_temporal_grid_layers_do_not_overwrite_each_other_in_js_queue():
    keys = {
        main_window.MainWindow._classify_js_call(
            f'window.setDemTemporalGrid("{layer}", {{"cells":[]}});'
        )
        for layer in ('local', 'global', 'candidates')
    }
    assert keys == {'dem_temporal_local', 'dem_temporal_global', 'dem_temporal_candidates'}
