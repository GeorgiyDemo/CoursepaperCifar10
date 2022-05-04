import os
import glob
import json
import requests
import shutil

def download_photo(url, file_name):
    url = url.replace('\\', '')
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
    else:
        print('Download failed')

class CarInfoProcessing:

    PATH = "./dumps/"
    def __init__(self) -> None:
        self.processing()

    def sep_one(self):
        """Шаг 1. Переименовывает и перемещает все файлы в одну папку"""
        os.mkdir
        if not os.path.exists(f"{self.PATH}all"):
            os.mkdir(f"{self.PATH}all")

        files_list = glob.glob(f"{self.PATH}dump*/search*", recursive=True)
        for i in range(len(files_list)):

            file_name = files_list[i]
            buf = file_name.split(os.sep)
            new_filename = f"{buf[0]}/{buf[1]}/all/{i}.json"
            os.rename(file_name, new_filename)
            print(f"{file_name} -> {new_filename}")

    def step_two(self):
        """Шаг 2. Засовывает все данные об авто в один файл, удаляет дубликаты"""
        cars_dict = {}
        car_counter = 0
        files_list = glob.glob(f"{self.PATH}all/*.json")
        for file in files_list:
            with open(file, "r") as f:
                data = json.loads(f.read())["data"]["cars"]
                if data is None:
                    continue

                car_counter += len(data)
                for current_car in data:
                    if current_car["id"] not in cars_dict:
                        cars_dict[current_car["id"]] = current_car

        print("Cars:", car_counter)
        print("Unique cars:", len(cars_dict))
        
        with open(f"{self.PATH}all/all_cars.json", "w") as f:
            f.write(json.dumps(cars_dict))
    
    def step_three(self):
        """3. Выкачивает все фотки и меняет ссылки на локльное имя файла"""
        with open(f"{self.PATH}all/all_cars.json", "r") as f:
            cars_dict = json.loads(f.read())
        
        if not os.path.exists(f"{self.PATH}photos"):
            os.mkdir(f"{self.PATH}photos")

        counter = 1
        for id, data in cars_dict.items():

            print(f"Working with car {id} ({counter}/{len(cars_dict)})")
            if data["mainPhoto"] is not None:
                is_current_photo_exists = None
                current_path = f"{self.PATH}photos/{id}_0.jpg"
                if not os.path.exists(current_path):
                    is_current_photo_exists = False
                    print("Downloading photo..")
                    download_photo(data["mainPhoto"][0]["url"], current_path)
                else:
                    is_current_photo_exists = True
                    print("Photo already downloaded")
                data["mainPhoto"][0]["url"] = current_path

                if not is_current_photo_exists and counter % 5 == 0:
                    print("Backed up to file all_cars.json")
                    with open(f"{self.PATH}all/all_cars.json", "w") as f:
                        f.write(json.dumps(cars_dict))
            
            counter += 1

    def processing(self):
        self.sep_one()
        self.step_two()
        self.step_three()
        print("Успешно загрузили все изображения, далее надо работать с MAIN.ipynb")
        

def main():
    car_info_processing = CarInfoProcessing()

if __name__ == "__main__":
    main()