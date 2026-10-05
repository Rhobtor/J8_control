from unittest.mock import Mock

from PySide6.QtWidgets import QApplication, QWidget

from gui.app import main_window


def test_main_window_initializes_planning_display_and_sends_dem_goal(monkeypatch):
    application = QApplication.instance() or QApplication([])
    monkeypatch.setattr(main_window, 'QWebEngineView', QWidget)
    monkeypatch.setattr(main_window.MainWindow, '_init_map', lambda self: None)
    monkeypatch.setattr(main_window.MainWindow, '_build_tab_video', lambda self: None)
    monkeypatch.setattr(main_window.MainWindow, '_build_tab_fsm_debug', lambda self: None)
    window = main_window.MainWindow(defer_ros_start=True)
    try:
        window._on_dem_coverage_status('DEM: cobertura disponible', True)
        assert window.lbl_dem_status.text() == 'DEM: cobertura disponible'

        window.mission_tab._planned = [(36.7164192, -4.4893259)]
        ros = Mock()
        window._ros = ros
        window.btn_plan_dem.click()
        ros.send_dem_goal.assert_called_once_with(36.7164192, -4.4893259)
        assert window.lbl_dem_status.text() == 'DEM: calculando ruta…'

        window._js_call = Mock()
        window._on_dem_path_received([])
        window._on_dem_coverage_status('DEM: sin posición', False)
        assert window.lbl_dem_status.text() == 'DEM: calculando ruta…'
        window._on_dem_path_received([[36.7164192, -4.4893259]])
        window._on_dem_planning_status_received({'state': 'READY'})
        assert window.lbl_dem_status.text() == 'DEM: ruta 1 pts'
    finally:
        window._ros = None
        window.deleteLater()
        application.sendPostedEvents()
