# Lost & Found Portal MU

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://shields.io/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org/)
[![Django](https://img.shields.io/badge/django-5.2.1-green)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌐 Live Demo
Access the live project [MU Lost & Found Portal](https://project-300-0.onrender.com/).

---

## 📖 Project Overview

The **Lost & Found Portal MU** is a comprehensive web application designed specifically for Metropolitan University's community. It provides an efficient platform for students, faculty, and staff (currently only for students) to report lost items, post found items, and facilitate the safe return of belongings through a streamlined claim management system.

### Key Objectives

- Centralize lost and found item management for the university
- Provide secure user authentication and profile management
- Enable efficient item searching and claiming processes
- Maintain detailed records and notifications for all transactions

---

## ✨ Key Features

### User Management

- **Secure Registration & Authentication**: Email-based registration with MU ID verification
- **Profile Management**: Comprehensive user profiles with department information
- **Role-based Access**: Different access levels for students, staff, and administrators

### Item Management

- **Post Lost Items**: Create detailed listings with descriptions, categories, and images
- **Post Found Items**: Report discovered items with location and contact details
- **Advanced Search**: Filter items by category, date, location, and keywords
- **Image Upload**: Support for multiple image formats with automatic optimization

### Claim System

- **Claim Requests**: Users can request to claim items with verification process
- **Notification System**: Real-time notifications for item claims and status updates
- **Approval Workflow**: Item owners can approve or reject claim requests
- **Communication Tools**: Built-in messaging between item owners and claimants

### Administrative Features

- **Content Moderation**: Admin interface for managing posts and users
- **Analytics Dashboard**: Track platform usage and success rates
- **Backup System**: Automatic backups for deleted posts and user data

---
## 🎥 Demo Video

Watch the full project demo on [MU Lost & Found Portal](https://youtu.be/QhHlWgT_syg).

---

## 🛠️ Tech Stack

| Component                 | Technology           | Version       |
| ------------------------- | -------------------- | ------------- |
| **Backend Framework**     | Django               | 5.2.1         |
| **Database**              | SQLite (Development) | Default       |
| **Database (Production)** | PostgreSQL/MySQL     | Configurable  |
| **Image Processing**      | Pillow               | Latest        |
| **Frontend**              | Django Templates     | HTML5/CSS3/JS |
| **Authentication**        | Django Auth          | Built-in      |
| **File Storage**          | Local/Cloud          | Configurable  |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- Git

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Project-300.git
cd Project-300
```

#### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Environment Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
MEDIA_ROOT=media/
STATIC_ROOT=static/
```

#### 5. Database Setup

```bash
cd lost_and_found_portal_MU

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

#### 6. Run Development Server

```bash
python manage.py runserver
```

#### 7. Access the Application

Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔌 API Reference

### Authentication Endpoints

#### `/signup/` - User Registration

**Description**: Registers a new user with university credentials.

**HTTP Method**: `POST`

**Request Body**:

```json
{
  "name": "string (required): Full name (minimum 3 characters)",
  "email": "string (required): Valid email address",
  "password": "string (required): Password (minimum 6 characters)",
  "mu_id": "string (required): Metropolitan University ID",
  "dept": "string (required): Department name",
  "phone": "string (optional): Contact number",
  "profileImage": "image (optional): User profile image"
}
```

**Example Request**:

```bash
curl -X POST http://127.0.0.1:8000/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@student.mu.edu",
    "password": "securepassword123",
    "mu_id": "222-115-201",
    "dept": "CSE"
  }'
```

**Example Response**:

```json
{
  "status": "success",
  "message": "User registered successfully",
  "user_id": 12345
}
```

---

#### `/signin/` - User Login

**Description**: Authenticates user credentials and establishes session.

**HTTP Method**: `POST`

**Request Body**:

```json
{
  "email": "string (required): User email address",
  "password": "string (required): User password"
}
```

**Example Response**:

```json
{
  "status": "success",
  "message": "Login successful",
  "user": {
    "id": 12345,
    "name": "John Doe",
    "email": "john.doe@student.mu.edu",
    "dept": "CSE"
  }
}
```

---

#### `/logout/` - User Logout

**Description**: Terminates user session and clears authentication.

**HTTP Method**: `GET`

**Authentication**: Required

**Example Response**:

```json
{
  "status": "success",
  "message": "Logout successful"
}
```

---

### Profile Management

#### `/user-profile/` - View Profile

**Description**: Retrieves current user's profile information.

**HTTP Method**: `GET`

**Authentication**: Required

**Example Response**:

```json
{
  "user": {
    "id": 12345,
    "name": "John Doe",
    "email": "john.doe@student.mu.edu",
    "mu_id": "222-115-201",
    "dept": "CSE",
    "phone": "+1234567890",
    "profileImage": "media/profile_images/profile.jpg",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

---

#### `/edit-profile/` - Update Profile

**Description**: Updates user profile information.

**HTTP Method**: `POST`

**Authentication**: Required

**Request Body**:

```json
{
  "name": "string (optional): Updated full name",
  "phone": "string (optional): Updated phone number",
  "email": "string (optional): Updated email"
}
```

---

### Item Management

#### `/create-post/` - Create Item Post

**Description**: Creates a new lost or found item listing.

**HTTP Method**: `POST`

**Authentication**: Required

**Request Body** (Form Data):

```
title: string (required) - Item title
description: string (required) - Detailed description
item_type: string (required) - "lost" or "found"
location: string (required) - Last known/found location
image: file (optional) - Item image
```

**Example Response**:

```json
{
  "status": "success",
  "message": "Item posted successfully",
  "item_id": 789,
  "post_url": "/details-post/789"
}
```

---

#### `/item/` - List All Items

**Description**: Retrieves paginated list of all items (lost and found).

**HTTP Method**: `GET`

**Query Parameters**:

- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10)
- `category`: Filter by category
- `search`: Search term

**Example Response**:

```json
{
  "items": [
    {
      "id": 789,
      "title": "iPhone 13 Pro",
      "category": "Electronics",
      "type": "lost",
      "location": "Library",
      "posted_by": "John Doe",
      "posted_at": "2024-01-20T14:30:00Z",
      "image_url": "/media/items/iphone_789.jpg"
    }
  ],
  "total_count": 45,
  "page": 1,
  "total_pages": 5
}
```

---

#### `/found-item/` - List Found Items

**Description**: Retrieves all items that have been found.

**HTTP Method**: `GET`

**Query Parameters**: Same as `/item/` endpoint

---

#### `/lost-item/` - List Lost Items

**Description**: Retrieves all items that are lost.

**HTTP Method**: `GET`

**Query Parameters**: Same as `/item/` endpoint

---

#### `/details-post/<item_id>` - Item Details

**Description**: Retrieves detailed information about a specific item.

**HTTP Method**: `GET`

**Path Parameters**:

- `item_id`: Unique identifier of the item

**Example Response**:

```json
{
  "item": {
    "id": 789,
    "title": "iPhone 13 Pro",
    "description": "Black iPhone 13 Pro with cracked screen protector",
    "type": "lost",
    "location": "Main Library, 2nd Floor",
    "posted_by": {
      "name": "John Doe",
      "email": "john.doe@student.mu.edu",
      "dept": "Computer Science"
    },
    "posted_at": "2024-01-20T14:30:00Z",
    "images": ["/media/items/iphone_789.jpg"],
    "status": "active",
    "claim_count": 3
  }
}
```

---

#### `/edit-post/<item_id>` - Edit Item Post

**Description**: Updates an existing item post (only by the original poster).

**HTTP Method**: `POST`

**Authentication**: Required (Must be item owner)

**Path Parameters**:

- `item_id`: Unique identifier of the item

**Request Body**: Same as create-post endpoint

---

#### `/delete-post/<item_id>` - Delete Item Post

**Description**: Soft deletes an item post with backup retention.

**HTTP Method**: `GET`

**Authentication**: Required (Must be item owner)

**Path Parameters**:

- `item_id`: Unique identifier of the item

**Example Response**:

```json
{
  "status": "success",
  "message": "Item post deleted successfully",
  "backup_id": "backup_789_20240120"
}
```

---

### Claim Management

#### `/claim-request/<item_id>` - Submit Claim Request

**Description**: Submits a claim request for a specific item.

**HTTP Method**: `POST`

**Authentication**: Required

**Path Parameters**:

- `item_id`: Unique identifier of the item to claim

**Request Body**:

```json
{
  "message": "string (optional): Additional message to item owner",
  "contact_preference": "string (optional): Preferred contact method"
}
```

**Example Response**:

```json
{
  "status": "success",
  "message": "Claim request submitted successfully",
  "claim_id": 456
}
```

---

#### `/found-notification/<item_id>` - Found Item Notification

**Description**: Notifies relevant users when a matching item is found.

**HTTP Method**: `GET`

**Authentication**: Required

**Path Parameters**:

- `item_id`: Unique identifier of the found item

---

### Notification System

#### `/notifications/` - View Notifications

**Description**: Retrieves user's notifications including claim requests and updates.

**HTTP Method**: `GET`

**Authentication**: Required

**Query Parameters**:

- `status`: Filter by status (unread, read, all)
- `type`: Filter by notification type

**Example Response**:

```json
{
  "notifications": [
    {
      "id": 123,
      "type": "claim_request",
      "title": "New claim request for your item",
      "message": "Someone wants to claim your iPhone 13 Pro",
      "item_id": 789,
      "from_user": "Jane Smith",
      "created_at": "2024-01-21T09:15:00Z",
      "is_read": false,
      "actions": [
        {
          "type": "accept",
          "url": "/accept_request/123/789"
        },
        {
          "type": "reject",
          "url": "/reject_request/123/789"
        }
      ]
    }
  ],
  "unread_count": 3
}
```

---

#### `/accept_request/<notification_id>/<item_id>` - Accept Claim

**Description**: Accepts a claim request for an item.

**HTTP Method**: `GET`

**Authentication**: Required (Must be item owner)

**Path Parameters**:

- `notification_id`: Unique identifier of the notification
- `item_id`: Unique identifier of the item

**Example Response**:

```json
{
  "status": "success",
  "message": "Claim request accepted",
  "next_steps": "Contact information shared with claimant"
}
```

---

#### `/reject_request/<notification_id>/<item_id>` - Reject Claim

**Description**: Rejects a claim request for an item.

**HTTP Method**: `GET`

**Authentication**: Required (Must be item owner)

**Path Parameters**:

- `notification_id`: Unique identifier of the notification
- `item_id`: Unique identifier of the item

---

#### `/clear_all/` - Clear All Notifications

**Description**: Marks all notifications as read for the current user.

**HTTP Method**: `GET`

**Authentication**: Required

**Example Response**:

```json
{
  "status": "success",
  "message": "All notifications cleared",
  "cleared_count": 7
}
```

---

## 📁 Project Structure

```
Project-300/
├── 📁 lost_and_found_portal_MU/
│   ├── 📁 app/                          # Main Django application
│   │   ├── 📄 models.py                 # Database models
│   │   ├── 📄 views.py                  # View controllers
│   │   ├── 📄 urls.py                   # URL routing
│   │   ├── 📄 forms.py                  # Django forms
│   │   ├── 📄 admin.py                  # Admin interface
│   │   └── 📁 migrations/               # Database migrations
│   ├── 📁 lost_and_found_portal_MU/     # Project configuration
│   │   ├── 📄 settings.py               # Django settings
│   │   ├── 📄 urls.py                   # Main URL configuration
│   │   └── 📄 wsgi.py                   # WSGI configuration
│   ├── 📁 templates/                    # HTML templates
│   │   ├── 📁 app/                      # App-specific templates
│   │   └── 📄 base.html                 # Base template
│   ├── 📁 static/                       # Static files (CSS, JS, images)
│   │   ├── 📁 css/                      # Stylesheets
│   │   ├── 📁 js/                       # JavaScript files
│   │   └── 📁 images/                   # Static images
│   ├── 📁 media/                        # User uploaded files
│   │   └── 📁 items/                    # Item images
│   ├── 📄 db.sqlite3                    # SQLite database (development)
│   ├── 📄 manage.py                     # Django management script
│   └── 📄 requirements.txt              # Python dependencies
├── 📄 .env.example                      # Environment variables template
├── 📄 .gitignore                        # Git ignore rules
├── 📄 LICENSE                           # License file
└── 📄 README.md                         # Project documentation
```

---

## 🧪 Testing

### Running Tests

```bash
# Navigate to project directory
cd lost_and_found_portal_MU

# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Categories

- **Unit Tests**: Model and form validation tests
- **Integration Tests**: View and URL routing tests
- **Authentication Tests**: User registration and login tests
- **API Tests**: Endpoint functionality and response validation

---

## 🔐 Security Features

### Authentication & Authorization

- **Session-based Authentication**: Secure user sessions with Django's built-in system
- **CSRF Protection**: Cross-site request forgery protection on all forms
- **Password Security**: Hashed passwords using Django's PBKDF2 algorithm
- **Permission Checks**: Role-based access control for sensitive operations

### Data Protection

- **Input Validation**: Server-side validation for all user inputs
- **SQL Injection Prevention**: ORM-based database queries
- **File Upload Security**: Restricted file types and size limits
- **XSS Protection**: Template auto-escaping and content sanitization

### Production Security Checklist

- [ ] Set `DEBUG = False` in production
- [ ] Use environment variables for sensitive settings
- [ ] Configure HTTPS and secure headers
- [ ] Implement rate limiting for API endpoints
- [ ] Regular security updates and dependency management
- [ ] Database access restrictions and backups

---

## 🚀 Deployment

### Environment Setup

1. **Production Settings**:

```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

2. **Static Files**:

```bash
python manage.py collectstatic --noinput
```

3. **Database Migration**:

```bash
python manage.py migrate --settings=settings.production
```

### Deployment Platforms

- **Render**: Fully compatible for quick deployment.
- **Heroku**: Ready for Heroku deployment with Procfile
- **DigitalOcean**: Docker containerization support
- **AWS**: EC2 and RDS compatible
- **Local Server**: Apache/Nginx configuration available

---

## 📊 Performance Optimization

### Database Optimization

- Indexed fields for fast searching
- Query optimization with select_related and prefetch_related
- Database connection pooling for production

### Caching Strategy

- Template fragment caching for common components
- Database query caching for frequently accessed data
- Static file compression and CDN integration

### Monitoring

- Django Debug Toolbar for development
- Application performance monitoring (APM) ready
- Error tracking and logging configuration

---

## 🤝 Contributing

We welcome contributions from the Metropolitan University community!

### Getting Started

1. **Fork the Repository**

   ```bash
   git clone https://github.com/yourusername/Project-300.git
   ```

2. **Create Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**

   - Follow Django coding standards
   - Add tests for new functionality
   - Update documentation as needed

4. **Submit Pull Request**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   git push origin feature/your-feature-name
   ```

### Development Guidelines

- **Code Style**: Follow PEP 8 standards
- **Testing**: Maintain test coverage above 80%
- **Documentation**: Update docs for any API changes
- **Commit Messages**: Use clear, descriptive commit messages

### Issue Reporting

Before creating an issue, please:

- Check existing issues for duplicates
- Provide detailed reproduction steps
- Include system information and error logs
- Use appropriate issue labels

---
## Future Work
- **Expand User Base:** Extend the platform to include faculty and staff, in addition to students.  
- **Mobile Integration:** Develop a mobile application for seamless access across devices.  
- **Real-Time Notifications:** Implement enhanced notifications via email and SMS for all users.  
- **Admin Dashboard:** Introduce a comprehensive admin dashboard for efficient item and user management.  
- **Unified Authentication:** Update the authentication system to integrate with the university’s central database for all users.

---


## 👥 Development Team

| Role                   | Name                    | Contact                                   |
| ---------------------- | ----------------------- | ----------------------------------------- |
| **Lead Developer**     | Sudipto Dey Himel       | [GitHub](https://github.com/himel5113) |
| **Backend Developer**  | Md. Tanimur Rahman      | [GitHub](https://github.com/tanim-mishkat)      |


## 🔄 Changelog

### Version 1.0.0 (Current)

- Initial release with core functionality
- User authentication and profile management
- Item posting and search capabilities
- Claim request system
- Notification management
- Admin interface

_Last Updated: August 2025_

> **Note**: This documentation is actively maintained. For the most up-to-date information, please refer to the project repository.
