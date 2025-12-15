import json


class Airplane:

    def __init__(self, model: str, seats: int, plane_range: int):
        self.__model = model
        self.__seats = seats
        self.__plane_range = plane_range

    def get_model(self):
        return self.__model

    def get_seats(self):
        return self.__seats

    def get_plane_range(self):
        return self.__plane_range

    def print_airplane_props(self):
        print(
            f"airplane model: {self.get_model()} has {self.get_seats()} available seats"
            f"and has {self.get_plane_range()} km max distance flight"
        )


class JSONPlaneAdapter:

    @classmethod
    def to_json(cls, obj: Airplane):
        if isinstance(obj, Airplane):
            return json.dumps({
                'model': obj.get_model(),
                'seats': obj.get_seats(),
                'range': obj.get_plane_range(),
                'class': obj.__class__.__name__,
                'methods': {
                    'get_model': obj.get_model(),
                    'get_seats': obj.get_seats(),
                    'get_range': obj.get_plane_range(),
                    'print_airplane_props': f'printed data {
                    [
                        f"airplane model: {obj.get_model()} has {obj.get_seats()} available seats",
                        f"and has {obj.get_plane_range()} km max distance flight"
                    ]
                    }',
                }
            })
        raise ValueError("Объект неподходящего класса.")

    @classmethod
    def from_json(cls, obj):
        obj = json.loads(obj)
        try:
            model = obj['model']
            seats = obj['seats']
            obj_range = obj['range']
            plane_obj = Airplane(model, seats, obj_range)
            return plane_obj
        except AttributeError:
            print(f'Неверная структура')
            return None


if __name__ == '__main__':
    plane = Airplane('Boeing 737-200', 110, 4000)
    plane_json = JSONPlaneAdapter.to_json(plane)
    print(plane_json)
    print()
    my_plane_obj = JSONPlaneAdapter.from_json(plane_json)
    my_plane_obj.print_airplane_props()