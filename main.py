import csv

csv.register_dialect('pipes', delimiter=',')


file_path = "C:\\Users\\WiktorPC\\Desktop\\EngineParts\\IMGS\\PhoneImgs\\ConvertedPhotos4phone\\BrakeFluid"
label = ""
left_up_coordinates_width = 0
left_up_coordinates_height = 0
right_down_coordinates_width = 0
right_down_coordinates_height = 0
type = "TRAINING"
image_height = 0
image_width = 0
data = []

with open('csv/brakes_fluid_csv.csv', 'r') as f:
    reader = csv.reader(f, dialect='pipes')
    for row in reader:
        print(row)
        image_width = row[6]
        image_height = row[7]
        label = row[0]
        left_up_coordinates_width = round(int(row[1])/ int(image_width), 3)
        left_up_coordinates_height = round(int(row[2])/int(image_height), 3)
        right_down_coordinates_width = round(int(row[3])/int(image_width), 3)
        right_down_coordinates_height = round(int(row[4])/int(image_height), 3)
        #data = [type, file_path + "\\" + row[5], label, str(left_up_coordinates_width), str(left_up_coordinates_height),'','',str(right_down_coordinates_width),str(right_down_coordinates_height),'','']
        data.append([type, file_path + "\\" + row[5], label, str(left_up_coordinates_width), str(left_up_coordinates_height),'','',str(right_down_coordinates_width),str(right_down_coordinates_height),'',''])


with open('csv/brakes_fluid_csv_output.csv', 'w', encoding='UTF8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)