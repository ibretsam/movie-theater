# Final Project (Capstone)

- [Movie Theater](#movie-theater)
    - [Technologies used](#technologies-used)
    - [Project requirements](#project-requirements)
    - [Key features](#key-features)
- [How to run](#how-to-run)
- [API](#api)
- [Source code tree](#source-code-tree)
- [Distinctiveness and Complexity](#distinctiveness-and-complexity)

## Movie Theater
This project is for the final project [Capstone](https://cs50.harvard.edu/web/2020/projects/final/cap) of the online course [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/). The website replicates the basic functions of a movie theater website, where users can register for an account, see which movies is showing, select times, choose a seat, book a ticket for a movie, and see their booking history.
This project uses Django as backend and ReactJS, Javascript (ES6), Bootstrap for frontend.

### Technologies used:
- Python
- Django
- Django Rest Framework
- Javascript (ES6)
- ReactJS
- React-Router-DOM
- Bootstrap


### Project requirements:
- Must be sufficiently distinct from the other projects in this course.
- Utilizes Django (with at lease one model) on the back-end and JavaScript on the front-end.
- All pages are mobile responsive.
- Uses ReactJS for frontend UI, only communicates with backend through API calls.
	- Uses `Hash Router` and `useNavigate` from [react-router-dom](http://reactrouter.com/) to routes and navigate through pages.
    - Uses `Fetch API` for all API calls to communicate with backend.
    - Uses [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) for CSS decoration.
- Uses [Django-Rest-Framework](https://www.django-rest-framework.org/) for API manage:
    - Uses `@api_view` decorator to response to API calls
    - Uses `ModelSerializer` to serialize all model query to return results
    - Implement [JWT Authentication](https://jwt.io/) to Django using [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) for [Django-Rest-Framework](https://www.django-rest-framework.org/)

### Key features:
- ReactJS for frontend UI
- JWT authentication for user
- ##### For user: 
    - Book a ticket for a movie as a user:
        1. Choose a movie
        2. Select screen date and time
        3. Select seat (Cannot choose the seat that has been taken by other user)
        4. Select ticket type
    - View your booked ticket
- ##### For administrator (Utilize Django admin):
    - Create new movie
    - Create new gernes
    - Create screen date and time for a movie
    - Create new theater (Every theater has the same 64 seats for now)
    - Manage ticket type and price for each types
    - Manage movies, genres, screens, seats, theaters, ticket types and bookings by user

## How to run
1. Clone this repo
```
git clone https://github.com/ibretsam/movie-theater.git
```
2. Create a virtual environment and activate it:

```
# Create a virtual environment
python3 -m venv venv

# Activate virtual environment
	# macOS:
	source venv/bin/activate
	# Windows:
	venv/Scripts/activate.bat
```
3. Install required python dependencies:
```
pip install -r requirements.txt
```

4. Navigate into main front-end foldder: 
```
cd front-end/movietheater
``` 

5. Install required Node dependencies:
```
npm install --legacy-peer-deps
```

6. Build React app:
```
npm run build
```
7. Navigate back to main project folder
```
cd ../..
```
8. And finally start the Django web server
```
python manage.py runserver
```


## API

#### WEBSITE API

###### GET MOVIES:
Returns an array of movies object

	'Endpoint': '/movies/',
	'method': 'GET',
	'body': None

###### GET SINGLE MOVIE:
Returns a single movie object

	'Endpoint': '/movies/id',
	'method': 'GET',
	'body': None

###### GET SCREEN
Returns an array of screen object of the movie object

	'Endpoint': '/movies/id/screen',
	'method': 'GET',
	'body': None

###### GET SINGLE SCREEN
Returns a single screen object

	'Endpoint': '/movies/id/screen/screenId',
	'method': 'GET',
	'body': None

###### GET SINGLE TICKET
Returns a single ticket_type object

	'Endpoint': '/ticket/ticketId',
	'method': 'GET',
	'body': None

###### CREATE SEAT & BOOKING
Create new seat object and new booking object

	'Endpoint': '/movies/id/screen/screenId/book',
	'method': 'POST',
	'headers': {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String,
        }
	'body': {'body': {booking_object}}

###### GET TAKEN SEAT
Returns an array of taken seat of the screen object that related to

	'Endpoint': '/movies/id/screen/screenId/getSeatsInfo',
	'method': 'POST',
	'headers': {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String,
        }
	'body': None

###### GET TICKET TYPES
Returns an array of ticket type of the screen object that related to

	'Endpoint': '/movies/id/screen/screenId/getTicketInfo',
	'method': 'POST',
	'headers': {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String,
        }
	'body': None

###### GET SINGLE BOOKING
Returns a single booking object

	'Endpoint': '/movies/id/screen/screenId/booking/bookingId',
	'method': 'POST',
	'headers': {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String,
        }
	'body': None

###### GET BOOKINGS
Returns an array of booking objects by a specific user

	'Endpoint': '/movies/id/screen/screenId/booking/bookingId/getSeatInfo',
	'method': 'POST',
	'body': None

#### AUTHENTICATION API
Authentication with [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) package for Django

###### REGISTER
Register a user with their username, email, password, confirm password

	'Endpoint': '/auth/register/'
	'method': 'POST'
	'body': {
		'username': String,
		'password': String,
		'confirmation': String, 
		'email': String
	}

###### GET TOKEN (LOGIN)
Return an authentication token if user credentials are correct

	'Endpoint': '/auth/token/'
	'method': 'POST'
	'body': {
		'username': String,
		'password': String
	}

###### GET REFRESH TOKEN
Return a refresh token every 4 minutes

	'Endpoint': '/auth/token/refresh/'
	'method': 'POST'
	'body': {'refresh': String}


## Source code tree
- 📁 `finalProject` - Main project dir
	- 📁 `capstone`
	- 📁 `front-end` - Frontend (ReactJS)
		- 📁 `movietheater`
			- 📁 `build` - React build folder (auto-created)
			- 📁 `node_modules` - Contains all node modules installed via `npm`
			- 📁 `public` - Defaul React files
			- 📁 `src` - Main React folder
				- 📁 `components` - React Components
					- 📄 `Header.js` - Header
					- 📄 `ListMovies.js` - To show all movies in homepage
					- 📄 `ListTicket.js` - To show all ticket types in booking page
					- 📄 `Theater.js` - Default theater page (64 seats)
				- 📁 `context` - React context
					- 📄 `AuthContext.js` - Authentication context (Login, Register, Update refresh token)
				- 📁 `pages` - All pages react components
					- 📄 `BookingPage.js` - For users to choose seat and ticket types
					- 📄 `ConfirmationPage.js` - For users to see their booking info
					- 📄 `LoginPage.js` - For users to login
					- 📄 `MoviePage.js` - Template for single movie page
					- 📄 `MoviesListPage.js` - Listing all movies page
					- 📄 `ProfilePage.js` - For users to see their booking history
					- 📄 `RegistrationPage.js` - For users to register an account
					- 📄 `ScreeningPage.js` - For users to choose date and time of a movie
				- 📁 `utils`
					- 📄 `PrivateRoute.js` - For config private routes (Only logged in users can go to these routes)
				- 📄 `App.css` - Main app CSS files
				- 📄 `App.js` - Main React component
				- 📄 `index.js` - React app entry
			- 📄 `package-lock.json` - React default file
			- 📄 `package.json` - Package manager file
			- 📄 `README.md` - React default file
	- 📁 `movieTheater` - Backend (Django)
		- 📁 `auth` - Authentication files
			- 📄 `serializers.py` - Serializer for authentication models
			- 📄 `urls.py` - Authentication urls
			- 📄 `views.py` - Authentication views
		- 📁 `migration` - Database migration files
		- 📄 `admin.py` - Register models in Django's admin panel.
		- 📄 `apps.py` - App configurations.
		- 📄 `models.py` - App models.
		- 📄 `serializers.py` - Serializers for app models
		- 📄 `tests.py` - App tests
		- 📄 `urls.py` - App urls
		- 📄 `views.py` - App views
	- 📄 `requirement.txt` - Required python dependency

## Distinctiveness and Complexity