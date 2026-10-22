SyncPlay

Problem

Gaming groups waste 30 to 45 minutes of every scheduled session arguing, cross-referencing, and guessing what multiplayer or co-op games everyone owns, has installed, and wants to play. This causes unnecessary pre-game friction, delays, and administrative overhead.

Users

PC gamers with disparate Steam libraries, Discord community organizers/party leaders, casual friend groups, and collegiate eSports or gaming clubs managing multiple concurrent members.

Solution

SyncPlay is a web-based multi-user Steam library matchmaker and game night coordinator built with Flask and React. Users can authenticate securely via Steam OpenID, create or join lobbies, automatically synchronize game libraries, calculate exact multi-way library intersections, filter titles by genre and player count, and vote on game selections in real time through an integrated voting dashboard. Each user's inventory and lobby data remain secure and user-scoped.

Features

Steam OpenID authentication and token handling

Automated Steam Web API integration to fetch owned game inventories (appid, title, playtime)

Create, join, and manage private game lobbies

Exact multi-way library intersection algorithm (O(N*M) hash map matching for 3, 4, or 10+ players simultaneously)

Track and filter shared game status:

Wishlist / Shortlist

Fully Owned by All Members

Partially Owned

Installed vs. Uninstalled status (where available)

Filter applications by:

Cooperative vs. competitive tags

Max player count limits

Genre and category tags

Search and sort shared library lists by playtime, title, or relevance

Paginated game lists for large library overlaps

Interactive dashboard with:

Total shared games count

Full-lobby ownership count

Real-time polling and voting board

Upcoming session time locks and schedules

User-scoped records and robust backend access controls

CSRF protection and secure session management for forms and endpoints

Automated tests for authentication, library synchronization, intersection algorithms, and lobby statistics

Technology
Python — core backend programming language

Flask — web application framework

Flask-SQLAlchemy — database integration and ORM

Flask-Login — session-based user authentication and session management

Flask-WTF — form handling and CSRF protection

SQLite — default local development database

PostgreSQL — supported through the DATABASE_URL environment variable

Steam Web API & OpenID 2.0 — external game inventory and authentication service

pytest — automated testing framework

Gunicorn — production WSGI server

Data Model
SyncPlay uses primary relational database models:

User — Steam ID, display name, avatar URL, authentication tokens, and account creation date

Lobby — lobby ID, host user ID, invite code, session lock time, and creation date

LobbyMember — mapping table linking users to lobbies with join state

GameVote — tracks user votes and shortlists for specific game IDs within a given lobby session

Each application and library sync query is securely scoped to authenticated lobby members.

Setup
Clone the repository:

git clone https://github.com/gilla5/syncplay.git
cd syncplay

Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure environment variables:
Create a .env file in the project root with your configuration details:

SECRET_KEY=replace-with-a-long-random-value
DATABASE_URL=sqlite:///instance/syncplay.db
STEAM_API_KEY=your-steam-web-api-key

(For PostgreSQL, replace DATABASE_URL with your PostgreSQL connection string.)

Run the application:

flask --app run.py run --debug

Run the tests:

pytest

Project Structure

syncplay/
├── app/
│   ├── auth/            # Steam OpenID authentication and session handling
│   ├── lobbies/         # Lobby management, creation, and member handling
│   ├── matchmaker/      # Multi-way library intersection algorithms and filtering
│   ├── voting/          # Real-time polling, shortlisting, and voting dashboard
│   ├── static/          # CSS assets and frontend branding
│   ├── templates/       # Jinja templates and dashboard views
│   ├── forms.py         # WTForms definitions and validation
│   ├── models.py        # User, Lobby, LobbyMember, and GameVote models
│   └── extensions.py    # Flask extensions setup
├── tests/               # Automated unit and integration tests
├── config.py            # Application configuration profiles
├── requirements.txt     # Python backend dependencies
└── run.py               # Application entry point

Roadmap
Potential future improvements include:

Discord webhook notifications for instant party session alerts

Cross-platform support for Epic Games Store, Xbox, and PlayStation libraries

Advanced prep checklists and session notes

Exportable game night reports and session history archives

Flask-Migrate database migration pipeline integration

Production Docker containerization and cloud deployment configuration

License
This project is developed as an individual project and academic showcase. Add a license file if the repository will be distributed publicly.
