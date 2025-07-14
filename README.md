# Event Scheduler

A simple yet powerful web application for scheduling and managing events, built with Flask and SQLAlchemy. It includes AI-powered features to make event creation faster and more intuitive.

## Features

- **Full CRUD Functionality:** Create, Read, Update, and Delete events.
- **Event Status Tracking:** Assign and update event statuses (Upcoming, Attending, Maybe, Declined).
- **Advanced Search:** Filter events by title, location, date range, or status.
- **Modern UI:** A clean and responsive user interface built with Bootstrap.
- **AI-Powered Location Suggestions:** Automatically suggests a location based on the event title.
- **AI-Powered Description Generation:** Automatically generates a relevant event description if one is not provided.

## Setup and Installation

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd event-scheduler-marwa
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    The project requires only a few packages. A `requirements.txt` file is provided for convenience.
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  Once the dependencies are installed, you can run the application with a single command:

    ```bash
    python flask-app.py
    ```

2.  The application will start in debug mode and be available at `http://127.0.0.1:5000`. Open this URL in your web browser.

## How to Use the AI Features

This application includes two smart features to help you create events more efficiently.

### 1. AI Location Suggester

When you are adding a new event, the application will analyze the **Title** as you type. If it recognizes keywords, it will automatically fill in the **Location** field for you.

**Examples:**

- **Title:** "Coffee meeting with team" -> **Location:** "Starbucks"
- **Title:** "Team lunch" -> **Location:** "Local Restaurant"
- **Title:** "Weekly planning meeting" -> **Location:** "Office, Conference Room A"

You can always edit or replace the suggested location.

### 2. AI Description Generator

If you leave the **Description** field empty when creating a new event, the application will automatically generate a relevant description for you.

**Example:**
If you create an event without a description, the AI might assign something like:

> "This event focuses on networking and professional growth."

This saves you time and ensures every event has a meaningful description.
