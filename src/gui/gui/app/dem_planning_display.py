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
        if self.state in ('PLANNING', 'WAITING_FOR_POSE'):
            return 'DEM: calculando ruta…', '#8a5a00'
        if self.state == 'REACHED':
            return 'DEM: objetivo alcanzado (1 m)', '#187a37'
        if self.state == 'FAILED':
            location = 'destino' if 'goal' in self.error else 'ruta'
            for marker, reason in (
                ('support residual', 'apoyo irregular'),
                ('support step', 'escalón excesivo'),
                ('pitch ', 'inclinación excesiva'),
                ('COLLISION', 'obstáculo'),
                ('hard blocking threshold', 'obstáculo'),
                ('unknown terrain', 'terreno sin datos'),
                ('terrain edge/drop', 'borde o desnivel'),
                ('goal has no admissible approach', 'sin acceso admisible'),
            ):
                if marker in self.error:
                    return f'DEM: {reason} ({location})', '#b42318'
            return 'DEM: sin ruta segura', '#b42318'
        if self.state == 'READY' or self.point_count > 0:
            text = f'DEM: ruta {self.point_count} pts' if self.point_count else 'DEM: ruta lista'
            return text, '#187a37'
        return None
