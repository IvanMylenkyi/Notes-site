
# Simple Notes Website

This project is a simple web application that allows users to create, read, edit, and delete notes. All notes are displayed on the main page as a list.

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/IvanMylenkyi/notes-site.git

2. Navigate to the project directory:

cd notes-site

3. Install dependencies using pip:

pip install -r requirements.txt

4. Apply migrations to create the database:

python manage.py migrate

## Usage

1. **Creating a Note**: Click on the "Create Task" button and enter the text of the note. Click the "Create" button to add the note.

2. **Reading a Note**: All created notes are displayed on the main page. Click the "More" to read it in full.

3. **Editing a Note**: To edit a note, click on the "More", then click on the "edit" button next to it. Make your changes and click the "Edit" button.

4. **Deleting a Note**: To delete a note, click on the "Delete" button next to it.


## Technologies

- Django - a web framework for building web applications with Python.
- HTML/CSS - for creating the user interface and interacting with users.

## Author

Author: Ivan Mylenkyi

Contact: mylenkyiivan@gmail.com

## License

This project is licensed under the [MIT License](LICENSE).
