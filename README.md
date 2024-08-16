Great! Given that your app also uses Redis and Celery, you should include sections on setting up and configuring these components in the `README.md` file. Here's an updated version of the README that incorporates Redis and Celery:

```markdown
# PoetryApp

PoetryApp is a Django-based web application that allows users to explore, create, and manage poetry. A key feature of this app is its integration with the Ollama Qwen2 model to summarize poems, providing insights and concise versions of the poetry content. The app also uses Celery for asynchronous task processing and Redis as the broker for Celery.

## Features

- **Browse Poetry**: Explore a collection of poems.
- **Create Poems**: Submit your own poetry.
- **Manage Poems**: Edit and delete your poems.
- **Summarize Poems**: Use Ollama Qwen2 to generate summaries of poems.
- **User Authentication**: Register, log in, and manage your account.
- **Asynchronous Tasks**: Process tasks asynchronously using Celery.

## Prerequisites

- Docker
- Poetry
- Python 3.8 or higher
- Django 4.0 or higher
- PostgreSQL 
- Redis
- Celery

## Setup Instructions

### Using Docker

To set up the project using Docker, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/samikshakhadka/PoetryApp.git
   cd PoetryApp
   ```

2. **Build and Run Docker Containers**

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers defined in your `docker-compose.yml` file. The application, Redis, and Celery workers will be up and running. The application will be accessible at `http://127.0.0.1:8000/`.

### Using Poetry

If you prefer to set up the project locally using Poetry, follow these instructions:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/samikshakhadka/PoetryApp.git
   cd PoetryApp
   ```

2. **Install Dependencies with Poetry**

   ```bash
   poetry install
   ```

3. **Activate the Poetry Shell**

   ```bash
   poetry shell
   ```

4. **Set Up Redis**

   Make sure you have Redis installed and running locally. You can download Redis from the [official website](https://redis.io/download) or use a Docker container.

   ```bash
   redis-server
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

8. **Start Celery Workers**

   In a new terminal, start the Celery worker:

   ```bash
   celery -A your_project_name worker --loglevel=info
   ```

   Replace `your_project_name` with the name of your Django project.

## Integrating Ollama Qwen2

To use the Ollama Qwen2 model for summarizing poems, follow these steps:

1. **Install Ollama CLI**

   Follow the installation instructions from the [Ollama documentation](https://ollama.com/docs) to install the Ollama CLI on your local machine.

2. **Download the Qwen2 Model**

   ```bash
   ollama install qwen2
   ```

   Ensure the model is properly installed and accessible.

3. **Configuration**

   Update your Django settings or environment variables to include the necessary configurations for the Ollama Qwen2 model.

## Usage

- **Register**: Create a new account by visiting the registration page.
- **Log In**: Access your account with your credentials.
- **Browse Poetry**: View poems in the collection.
- **Create Poems**: Add new poetry through your profile.
- **Manage Poems**: Edit or delete your poems as needed.
- **Summarize Poems**: Use the Ollama Qwen2 integration to generate summaries of poetry.
- **Asynchronous Tasks**: Celery will handle background tasks such as summarizing poems and other long-running processes.

## API Documentation

For details on the available API endpoints, refer to the Swagger documentation, accessible at `/swagger/` after starting the server.

## Running Tests

To ensure everything is working correctly, run the following command:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! To contribute to PoetryApp:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.


## Contact

For questions or feedback, please contact:

- **Name**: Samiksha Khadka
- **Email**: [samikshakhadka0.com](mailto:your-email@example.com)

```

This README includes instructions for Docker setup, local setup using Poetry, Redis setup, Celery configuration, and integrating the Ollama Qwen2 model. 