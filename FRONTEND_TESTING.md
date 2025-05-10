# Frontend Testing Guide

## Prerequisites

1. Node.js and npm installed
2. Backend server running at http://localhost:5000
3. MongoDB connection established

## Setup Instructions

1. Navigate to the client directory:
```bash
cd client
```

2. Install dependencies:
```bash
npm install
```

3. Start the frontend development server:
```bash
npm start
```

The frontend application will start at http://localhost:3000

## Testing Scenarios

### 1. User Registration

1. Navigate to http://localhost:3000/register
2. Fill in the registration form with the following test data:
   ```
   Email: test@example.com
   Password: test123
   First Name: Test
   Last Name: User
   Education:
     - Degree: BS
     - Field: Computer Science
   Work Experience:
     - Company: Test Company
     - Position: Software Engineer
   Skills: Python, Web Development, JavaScript
   ```
3. Click "Register"
4. Expected: Redirected to login page with success message

### 2. User Login

1. Navigate to http://localhost:3000/login
2. Use one of the following test accounts:
   ```
   Account 1:
   Email: user1@example.com
   Password: password1

   Account 2:
   Email: user25@example.com
   Password: password25

   Account 3:
   Email: user50@example.com
   Password: password50
   ```
3. Click "Login"
4. Expected: Redirected to dashboard with user profile

### 3. Job Recommendations

1. After logging in, you should see the dashboard
2. Check the "Recommended Jobs" section
3. Verify that:
   - Job cards are displayed
   - Each job shows:
     - Company name
     - Job title
     - Location
     - Required skills
4. Click on a job card to view details
5. Expected: Detailed job information page opens

### 4. Save/Unsave Jobs

1. From the job recommendations:
   - Click the "Save" button on a job card
   - Expected: Button changes to "Saved"
2. Navigate to "Saved Jobs" section
3. Verify the job appears in saved jobs
4. Click "Unsave" on the job
5. Expected: Job is removed from saved jobs

### 5. Profile Management

1. Click on your profile icon
2. Select "Account Settings"
3. Test the following:
   - View current profile information
   - Update education details
   - Update work experience
   - Add/remove skills
4. Click "Save Changes"
5. Expected: Profile updates are saved

### 6. Job Search

1. Use the search bar at the top
2. Test different search criteria:
   - Job title
   - Company name
   - Location
   - Skills
3. Verify search results are relevant
4. Test filters:
   - Job type
   - Experience level
   - Location
   - Company size

### 7. Responsive Design

Test the application on different screen sizes:
1. Desktop (1920x1080)
2. Laptop (1366x768)
3. Tablet (768x1024)
4. Mobile (375x667)

Verify that:
- Navigation menu is accessible
- Content is properly formatted
- No horizontal scrolling
- Touch targets are appropriately sized

### 8. Error Handling

Test various error scenarios:
1. Invalid login credentials
2. Network disconnection
3. Invalid form inputs
4. Session timeout
5. Server errors

Expected behavior:
- Clear error messages
- Graceful fallbacks
- Proper redirection
- Session management

## Common Issues and Solutions

1. **CORS Errors**
   - Ensure backend server is running
   - Check proxy settings in package.json
   - Verify API endpoints are correct

2. **Authentication Issues**
   - Clear browser cache and cookies
   - Check JWT token in localStorage
   - Verify token expiration

3. **Data Loading Issues**
   - Check network tab in browser dev tools
   - Verify API responses
   - Check MongoDB connection

4. **UI Rendering Problems**
   - Clear browser cache
   - Check console for errors
   - Verify all dependencies are installed

## Testing Tools

1. **Browser Developer Tools**
   - Network tab for API calls
   - Console for errors
   - Application tab for storage
   - Elements tab for UI inspection

2. **React Developer Tools**
   - Component inspection
   - Props verification
   - State management

3. **Postman/Insomnia**
   - API endpoint testing
   - Request/response verification
   - Authentication testing

## Reporting Issues

When reporting issues, include:
1. Steps to reproduce
2. Expected behavior
3. Actual behavior
4. Browser/device information
5. Screenshots/videos
6. Console errors
7. Network request/response data 