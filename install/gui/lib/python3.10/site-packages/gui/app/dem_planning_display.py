from dataclasses import dataclass


@dataclass
class DemPlanningDisplay:
    state: str = ''
    point_count: int = 0
    error: str = ''

    def planning(self) -> None:
        self.state = 'PLANNING'
        self.point_count = 0
        self.error = ''

    def receive_state(self, state: str, error: str = '') -> None:
        self.state = state
        self.error = error if state == 'FAILED' else ''

    def receive_path(self, point_count: int) -> None:
        self.point_count = point_count

    def status(self) -> tuple[str, str] | None:
        if self.state == 'PLANNING':
            return 'DEM: calculando ruta…', '#8a5a00'
        if self.state == 'FAILED':
            return 'DEM: sin ruta segura', '#b42318'
        if self.state == 'READY' or self.point_count > 0:
            text = f'DEM: ruta {self.point_count} pts' if self.point_count else 'DEM: ruta lista'
            return text, '#187a37'
        return None
