import csv

def open_file(file_name):
    # opens a csv file (maybe also has error handling)

def transform_user_details(csv_file_name):
    # use the open file function
    new_user_data = []
    with open(csv_file_name, newline='') as csvfile:
        user_details = csv.reader(csvfile, delimiter=',')

        for user in user_details:
            transformation = []
            transformation.append(user[1]) # name
            transformation.append(user[2]) # last name
            transformation.append(user[4]) # email
            new_user_data.append(transformation)
    return new_user_data

def create_new_csv(old_data="user_details.csv", new_file_name="new_user_details.csv"):
    new_user_data = transform_user_details(old_data)
    new_file = open(new_file_name, "w")

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_csv()