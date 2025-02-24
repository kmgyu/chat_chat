# Chat Chat

## Overview
Chat Chat is a Django-based real-time chat service inspired by platforms like KakaoTalk and Discord. Unlike traditional chat applications, it structures chat rooms as posts, allowing users to join and participate in conversations based on categorized topics.

## Features
- Real-time messaging using Django Channels and WebSockets
- Chat rooms structured like posts, allowing users to join based on interest
- User authentication and session management
- Message persistence via a database
- WebSocket-based real-time updates for seamless communication

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django 4.x
- Django Channels
- Redis (for WebSocket channel layers)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/kmgyu/chat_chat.git
   cd chat_chat
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
1. Open a browser and navigate to `http://127.0.0.1:8000`
2. Register or log in to create and join chat rooms
3. Start real-time conversations with other users

## WebSocket Implementation
- WebSockets are used to manage real-time messages.
- Django Channels handles WebSocket connections and message broadcasting.
- Redis is used as a channel layer to manage real-time data flow efficiently.

## Folder Structure
```
chat_chat/
│── config/          # Project configuration files
│── ws_chat/         # Core chat application
│── templates/       # HTML templates
│── requirements.txt # Dependency list
│── manage.py        # Django management script
```

## Future Enhancements
- Implement user roles and permissions in chat rooms
- Add support for multimedia messages
- Improve UI/UX with frontend frameworks

## Contributions
Contributions are welcome! Please follow the standard GitHub workflow:
1. Fork the repository
2. Create a new feature branch
3. Commit changes and push to your fork
4. Submit a pull request

## License
This project is licensed under the MIT License.

