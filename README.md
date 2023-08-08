# Pet Guardian: A Django Pet Rescue App

Pet Guardian is a web application built using the Django framework that helps connect pet owners and animal lovers to report and find lost pets. The app provides a platform for users to report lost or found pets, view a list of lost pets, and interact with the pet community.

## Work in Progress

This project is currently in development. New features and improvements are being added regularly. Feel free to contribute, and stay tuned for updates!


## Features

- Report Lost or Found Pets: Users can fill out a form to report lost or found pets, providing details about the pet, its description, and location.
- Lost Pets List: A list of lost pets is displayed on the main page, showing information about each pet that is currently reported as lost.
- User Profiles: Users can create profiles and edit their personal information.
- Admin Dashboard: Admin users have access to an admin dashboard for managing pets, lost pet reports, and user accounts.
- Pet Owner Dashboard: Pet owners can manage their own pets and lost pet reports.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/petguardian.git
   cd petguardian
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the app in your browser at `http://localhost:8000/`.

## Usage

1. Visit the home page to view a list of lost pets and submit a lost or found pet report.
2. Register or log in to create a user profile and manage your pets and reports.
3. Admin users can access the admin dashboard at `http://localhost:8000/admin/`.

## Contributing

Contributions are welcome! If you'd like to contribute to Pet Guardian, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).
