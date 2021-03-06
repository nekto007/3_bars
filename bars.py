import json
import sys
import os


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file_json:
        json_loaded = json.load(file_json)
    return json_loaded


def get_coordinates(bar):
    return bar["geometry"]["coordinates"]


def get_seats_count(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_name(bar):
    return bar["properties"]["Attributes"]["Name"]


def get_address(bar):
    return bar["properties"]["Attributes"]["Address"]


def get_biggest_bar(bars):
    return max(bars, key=get_seats_count)


def get_smallest_bar(bars):
    return min(bars, key=get_seats_count)


def get_closest_bar(bars, your_coordinate):
    return min(bars, key=lambda
        bar: get_distance_between_two_points(
        get_coordinates(bar), your_coordinate))


def get_distance_between_two_points(bar_coordinate, your_coordinate):
    try:
        return (bar_coordinate[0] - your_coordinate[0]) ** 2 + (
                bar_coordinate[1] - your_coordinate[1]) ** 2
    except TypeError:
        print("Координаты введены некорректно")


def get_user_coordinates():
    try:
        longitude = float(input("Введите долготу: "))
        latitude = float(input("Введите широту: "))
        return longitude, latitude
    except (TypeError, ValueError):
        print("Координаты введены некорректно")


def get_result(your_coordinate, bars):
    selected_bars = {
        "Самый большой бар:": get_biggest_bar(bars),
        "Самый маленький бар:": get_smallest_bar(bars),
        "Самый ближайший бар:": get_closest_bar(bars, your_coordinate)
    }
    for title, bar in selected_bars.items():
        print("{} {}. Находиться по адресу: {} и может вмещать посетителей: {}".format(
            title, get_name(bar), get_address(bar), get_seats_count(bar)))


if __name__ == "__main__":
    try:
        bars = load_data(sys.argv[1])["features"]
    except (FileNotFoundError, IndexError):
        print("Некоректно указан путь к файлу или файл не существует")
    except json.decoder.JSONDecodeError:
        print("Не корректное содержимое JSON файла")
    else:
        your_coordinate = get_user_coordinates()
        get_result(your_coordinate, bars)
