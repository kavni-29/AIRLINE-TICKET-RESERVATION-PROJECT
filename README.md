# Airline Reservation System

A comprehensive Python-based airline reservation and management system with both console and GUI interfaces. This system provides complete flight management, booking, and passenger tracking capabilities.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Quick Start Guide](#quick-start-guide)
- [Detailed Usage](#detailed-usage)
- [Data Structure](#data-structure)
- [File Formats](#file-formats)
- [User Workflows](#user-workflows)
- [Technical Documentation](#technical-documentation)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Airline Reservation System is a dual-interface application designed to manage flight schedules, passenger bookings, seat allocations, and reservations for multiple aircraft. It provides separate interfaces for administrators and end-users, ensuring proper role-based access and functionality.

### Key Capabilities

- **Multi-Aircraft Management**: Support for multiple aircraft with different seating configurations
- **Flight Scheduling**: Add, view, and delete flight schedules
- **Passenger Booking**: Complete booking workflow with seat selection
- **Reservation System**: Hold seats before final booking confirmation
- **Ticket Generation**: Print formatted tickets with booking details
- **Search & Filtering**: Search flights, passengers, and reservations by multiple criteria

### Interfaces

1. **Console Interface** (`airline_console.py`): Full-featured text-based interface with all functionalities
2. **GUI Interface** (`airline_gui.py`): Modern Tkinter-based graphical interface for core operations

---

## Features

### Admin Features

#### Flight Management
- **View All Flights**: Display complete flight schedules across all aircraft
- **Add Flight**: Create new flight schedules with pricing for all classes
- **Delete Flight**: Remove flights and associated passenger bookings
- **Auto Flight Numbering**: Sequential flight number generation (KR1000, KR1001, etc.)

#### Passenger Management
- **View Passenger Details**: Filter by Flight Number, PNR, or Name
- **Track Bookings**: Complete passenger information including seat assignments
- **Booking Analytics**: See booked seats by class

#### Reservation Management
- **View Reservations**: Track waiting/reserved seats
- **Filter Options**: Search by multiple criteria
- **Status Tracking**: Monitor reservation statuses

### User Features

#### Flight Search & Booking
- **Schedule Check**: Search flights by origin and destination
- **Date-based Search**: Filter flights by departure date
- **Class Selection**: Choose Economy, Business, or First Class
- **Seat Selection**: Interactive seat selection by row and number
- **Real-time Availability**: Check seat availability before booking

#### Ticket Management
- **Instant Booking**: Book tickets with immediate confirmation
- **Print Tickets**: Generate formatted tickets using PNR
- **Reservation System**: Reserve seats before final booking
- **Cancellation**: Cancel bookings and release seats

#### Advanced Features
- **Auto PNR Generation**: Unique Passenger Name Record numbers
- **Seat Mapping**: Visual seat layout (A-K rows, 1-3 seats per row)
- **Class-based Pricing**: Different pricing for Economy/Business/First Class
- **Timestamp Tracking**: Record booking date and time

---

## System Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
├──────────────────────────┬──────────────────────────────────┤
│   Console Interface      │      GUI Interface (Tkinter)     │
│   (airline_console.py)   │      (airline_gui.py)            │
└──────────────┬───────────┴──────────────┬───────────────────┘
               │                          │
               ├──────────────────────────┤
               │    Business Logic Layer   │
               │  - AirlineReservation    │
               │    System Class          │
               │  - Data Validation       │
               │  - File Operations       │
               └──────────┬───────────────┘
                          │
               ┌──────────┴───────────┐
               │   Data Storage Layer │
               │   (CSV Files)        │
               ├──────────────────────┤
               │ • AIRCRAFT.CSV       │
               │ • {AIRCRAFT}.csv     │
               │ • PASSENGER          │
               │   DETAILS.CSV        │
               │ • RESERVATION.CSV    │
               └──────────────────────┘
```

### Component Description

#### 1. Interface Layer
- **Console Interface**: Full CLI with menu-driven navigation
- **GUI Interface**: Tkinter-based windowed application with tabs

#### 2. Business Logic Layer
- **AirlineReservationSystem Class**: Core backend operations
- **Validation Functions**: Input sanitization and verification
- **File Management**: CSV read/write operations

#### 3. Data Layer
- **CSV-based Storage**: Lightweight, portable data storage
- **Relational Structure**: Linked data across multiple files

---

## Installation

### Prerequisites
```bash
Python 3.7 or higher
```

### Required Libraries
```bash
# Core libraries (usually pre-installed)
- tkinter (for GUI)
- csv
- datetime
- os

# Third-party library (for console interface)
- tabulate
```

### Installation Steps

#### 1. Clone or Download the Project
```bash
git clone https://github.com/yourusername/airline-reservation-system.git
cd airline-reservation-system
```

#### 2. Install Dependencies
```bash
# Install tabulate for console interface
pip install tabulate

# Or using requirements.txt
pip install -r requirements.txt
```

#### 3. Verify Installation
```bash
# Test console interface
python airline_console.py

# Test GUI interface
python airline_gui.py
```

---

## 🚀 Quick Start Guide

### Initial Setup (First Run)

#### Step 1: Launch the Application

**For GUI:**
```bash
python airline_gui.py
```

**For Console:**
```bash
python airline_console.py
```

#### Step 2: Add Aircraft Configuration

**Using GUI:**
1. Go to `Tools` → `Add Aircraft`
2. Fill in the form:
   - **Aircraft Name**: BOEING777 (alphanumeric, will be uppercase)
   - **Total Capacity**: 300
   - **Economy Seats**: 200
   - **Business Seats**: 75
   - **First Class Seats**: 25
3. Click "Add Aircraft"

**Using Console:**
1. Manually edit `AIRCRAFT.CSV`:
```csv
AIRCRAFT,CAPACITY,ECONOMY,BUSINESS,FIRST CLASS
BOEING777,300,200,75,25
AIRBUS380,400,250,100,50
```

#### Step 3: Add Your First Flight

**Using GUI:**
1. Go to `Admin Panel` → `Add Flight`
2. Fill in flight details:
   - **Aircraft Name**: BOEING777
   - **Day**: 15
   - **Month**: 12
   - **Year**: 24
   - **From**: Delhi
   - **To**: Mumbai
   - **Departure Time**: 10:30
   - **Arrival Time**: 12:45
   - **Economy Price**: 5000
   - **Business Price**: 12000
   - **First Class Price**: 25000
3. Click "Add Flight"

**Using Console:**
1. Select Option 1 (ADMIN)
2. Select Option 2 (ADD A FLIGHT)
3. Follow the prompts

#### Step 4: Search and Book

**User Side:**
1. Go to `User Panel` → `Flight Schedule`
2. Enter origin and destination
3. View available flights
4. Use PNR to print tickets (if already booked)

---

## 📖 Detailed Usage

### Admin Operations

#### 1. View All Flights

**Purpose**: Display all scheduled flights across all aircraft

**Steps:**
1. Select `Admin Panel` → `View Flights`
2. Click `Refresh Flights` button
3. View flight details in the text area

**Output Example:**
```
Fl_No    | Aircraft | Day | Month | Year | From   | To     | Departure | Arrival
---------|----------|-----|-------|------|--------|--------|-----------|--------
KR1000   | BOEING777| 15  | Dec   | 24   | Delhi  | Mumbai | 10:30     | 12:45
KR1001   | AIRBUS380| 16  | Dec   | 24   | Mumbai | Delhi  | 14:00     | 16:15
```

#### 2. Add a Flight

**Input Fields:**
- **Aircraft Name**: Must exist in AIRCRAFT.CSV (uppercase)
- **Day**: 1-31
- **Month**: 1-12 (converted to Jan-Dec)
- **Year**: Two-digit format (e.g., 24 for 2024)
- **From/To**: City names (will be title-cased)
- **Times**: 24-hour format (HH:MM)
- **Prices**: Must satisfy: Economy < Business < First Class

**Validation:**
- Aircraft must exist in system
- All fields mandatory
- Price hierarchy must be maintained
- Valid date ranges

**Auto-Generated:**
- Flight Number (Format: KR + sequential number)
- Seat availability counters (initialized to 0)
- Seat map (all seats marked as available)

#### 3. Delete a Flight

**Process:**
1. Enter flight number (e.g., KR1000)
2. System removes flight from aircraft CSV
3. System removes all associated passenger bookings
4. Confirmation message displayed

**Cascading Effects:**
- Passenger bookings are deleted
- Seat allocations are freed
- Reservation records are removed

#### 4. View Passenger Details

**Filter Options:**
- **By Flight Number**: See all passengers on a specific flight
- **By PNR**: Find a specific passenger's booking
- **By Name**: Search passengers by name

**Displayed Information:**
```
Fl_No | PNR   | Seat | From  | To    | Name          | Age | Sex | Address | Phone     | Amount | Class
------|-------|------|-------|-------|---------------|-----|-----|---------|-----------|--------|------
KR1000| 10001 | A1   | Delhi | Mumbai| JOHN DOE      | 35  | M   | 123 St  | 9876543210| 5000   | E
```

#### 5. View Reservations

**Purpose**: Track reserved (but not confirmed) seats

**Filter Options:** Same as passenger details

**Status Types:**
- **Waiting**: Reservation pending confirmation
- **Confirmed**: Booking completed

---

### User Operations

#### 1. Check Flight Schedule

**Purpose**: Search for available flights between two cities

**Steps:**
1. Enter origin city (e.g., Delhi)
2. Enter destination city (e.g., Mumbai)
3. View matching flights with availability

**Search Results Include:**
- Flight number and aircraft
- Departure date and time
- Arrival time
- Available seats by class
- Pricing by class

#### 2. Book a Ticket (Console Only)

**Full Booking Flow:**

##### Step 1: Search Flights
```
From: Delhi
To: Mumbai
Date: 15-Dec-24
```

##### Step 2: View Available Flights
```
Flights displayed with seat availability
```

##### Step 3: Select Flight
```
Enter Flight Number: KR1000
```

##### Step 4: Enter Passenger Details
```
Name: John Doe
Age: 35
Sex: M (Male), F (Female), O (Other)
Address: 123 Main Street, Delhi
Phone: +91-9876543210
```

##### Step 5: Choose Class
```
1. Economy (E)
2. Business (B)
3. First Class (F)
Choice: 1
```

##### Step 6: Seat Selection

**Seat Layout:**
```
First Class:    A, B, C (3 seats per row)
Business:       D, E, F (3 seats per row)
Economy:        G, H, I, J, K (3 seats per row)
```

**Selection:**
```
Choose Row: H
Choose Seat Number: 2
Result: Seat H2 selected
```

##### Step 7: Confirmation
```
PNR Generated: 10001
Booking Time: 21/11/24 14:30:25
Payment: ₹5000
Status: Confirmed
```

##### Step 8: Ticket Print
```
Ticket automatically displayed/can be reprinted using PNR
```

#### 3. Print Ticket

**Requirements:** Valid PNR number

**Steps:**
1. Select `Print Ticket`
2. Enter PNR (e.g., 10001)
3. Ticket displayed in formatted layout

**Ticket Format:**
```
--------------------------------------------------------------------------------
Booked on: 21/11/24 14:30:25
Fly Air Airlines
PASSENGER TICKET
--------------------------------------------------------------------------------

Ticket No.:     TN10001              Flight No.:  KR1000
Seat:           H2                   Name:        JOHN DOE
Date:           15-Dec-24            Status:      Confirmed
From:           Delhi                To:          Mumbai
Departure:      10:30                Arrival:     12:45
Class:          E                    Fare:        5000

--------------------------------------------------------------------------------
```

#### 4. Cancel Flight (Console Only)

**Steps:**
1. Enter PNR number
2. System verifies booking exists
3. Seat is released (marked as available)
4. Passenger record removed
5. Seat counter decremented

**Effects:**
- Seat becomes available for other passengers
- Full refund (system deletes record)
- Reservation record removed if exists

#### 5. Make a Reservation (Console Only)

**Purpose**: Hold a seat without immediate payment

**Process:**
1. Similar to booking flow
2. Seat marked as 'R' (Reserved) instead of '1' (Booked)
3. Status: "Waiting"
4. Can be confirmed later or cancelled

**Seat States:**
- `0`: Available
- `1`: Booked
- `R`: Reserved

#### 6. Book Reserved Ticket (Console Only)

**Steps:**
1. Enter PNR of reservation
2. System checks if seat is reserved
3. Converts reservation to confirmed booking
4. Seat marked as '1' (Booked)
5. Status updated to "Confirmed"

#### 7. Cancel Reservation (Console Only)

**Process:**
1. Enter PNR
2. System removes reservation
3. Seat becomes available ('0')
4. Passenger and reservation records deleted

---

## 📊 Data Structure

### Database Schema (CSV-Based)

#### 1. AIRCRAFT.CSV
**Purpose**: Master list of aircraft configurations
```csv
AIRCRAFT,CAPACITY,ECONOMY,BUSINESS,FIRST CLASS
BOEING777,300,200,75,25
AIRBUS380,400,250,100,50
```

**Fields:**
- `AIRCRAFT`: Unique aircraft identifier (alphanumeric)
- `CAPACITY`: Total passenger capacity
- `ECONOMY`: Number of economy class seats
- `BUSINESS`: Number of business class seats
- `FIRST CLASS`: Number of first class seats

**Constraints:**
- CAPACITY ≥ ECONOMY + BUSINESS + FIRST CLASS
- All fields mandatory
- AIRCRAFT must be unique

#### 2. {AIRCRAFT_NAME}.csv
**Purpose**: Flight schedules for each aircraft

**Example**: `BOEING777.csv`
```csv
Fl_No,AIRCRAFT,DAY,MONTH,YEAR,FROM,TO,DEPARTURE,ARRIVAL,SEATS(E),SEATS(B),SEATS(F),AMT(E),AMT(B),AMT(F),A,B,C,D,E,F,G,H,I,J,K
KR1000,BOEING777,15,Dec,24,Delhi,Mumbai,10:30,12:45,45,12,3,5000,12000,25000,001A,000B,000C,000D,111E,000F,010G,120H,000I,000J,000K
```

**Fields:**
- `Fl_No`: Unique flight number (KR + number)
- `AIRCRAFT`: Aircraft name (links to AIRCRAFT.CSV)
- `DAY`: Day of month (1-31)
- `MONTH`: Month name (Jan-Dec)
- `YEAR`: Two-digit year
- `FROM`: Origin city
- `TO`: Destination city
- `DEPARTURE`: Departure time (HH:MM)
- `ARRIVAL`: Arrival time (HH:MM)
- `SEATS(E/B/F)`: Booked seat count by class
- `AMT(E/B/F)`: Ticket price by class
- `A-K`: Seat map (4-character format per row)

**Seat Map Format:**
Each column (A-K) represents a row of 3 seats (positions 1, 2, 3).
Format: `XYZW` where:
- `X`: Seat 1 status (0=available, 1=booked, R=reserved)
- `Y`: Seat 2 status
- `Z`: Seat 3 status
- `W`: Row identifier (A-K)

Example: `120H` means:
- H1: Booked (1)
- H2: Reserved (R)
- H3: Available (0)
- Row: H

#### 3. PASSENGER DETAILS.CSV
**Purpose**: All confirmed passenger bookings
```csv
Fl_No,PNR,SEAT,FROM,TO,NAME,AGE,SEX,ADDRESS,PHONE,AMT,CLASS
KR1000,10001,H2,Delhi,Mumbai,JOHN DOE,35,M,123 Main St,9876543210,5000,E
KR1000,10002,A1,Delhi,Mumbai,JANE SMITH,28,F,456 Oak Ave,9876543211,25000,F
```

**Fields:**
- `Fl_No`: Flight number (links to aircraft CSV)
- `PNR`: Unique Passenger Name Record (10000+)
- `SEAT`: Assigned seat (e.g., H2)
- `FROM`: Origin
- `TO`: Destination
- `NAME`: Passenger name (uppercase)
- `AGE`: Passenger age (18+)
- `SEX`: M/F/O
- `ADDRESS`: Full address
- `PHONE`: Contact number
- `AMT`: Ticket price paid
- `CLASS`: E/B/F

**Constraints:**
- PNR must be unique
- Age ≥ 18
- Flight must exist
- Seat must be available

#### 4. RESERVATION.CSV
**Purpose**: Reserved (not yet confirmed) bookings
```csv
Fl_No,PNR,AIRCRAFT,DATE,FROM,TO,SEAT,NAME,AGE,PHONE,CLASS,FARE,STATUS
KR1001,10003,AIRBUS380,16-Dec-24,Mumbai,Delhi,D2,ALICE BROWN,32,9876543212,B,12000,Waiting
```

**Fields:**
- Similar to PASSENGER DETAILS
- `AIRCRAFT`: Aircraft name
- `DATE`: Formatted date (DD-Mon-YY)
- `STATUS`: "Waiting" or "Confirmed"

**Purpose:**
- Hold seats temporarily
- Allow payment processing time
- Can be converted to confirmed booking

---

## 🔄 User Workflows

### Workflow 1: Complete Booking Process
```
┌─────────────────┐
│  Start: User    │
│  Wants to Book  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Check Schedule │
│  (Origin/Dest)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ View Available  │
│    Flights      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Select Flight   │
│ Enter Passenger │
│    Details      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Choose Class &  │
│  Select Seat    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ System Validates│
│ & Checks Avail. │
└────────┬────────┘
         │
         ▼
    ┌───┴───┐
    │Available?│
    └───┬───┘
  Yes   │   No
    ▼   │   ▼
┌─────────┐ ┌─────────────┐
│ Generate│ │Show Error & │
│   PNR   │ │Ask to Retry │
└────┬────┘ └──────┬──────┘
     │             │
     ▼             │
┌─────────┐        │
│ Update  │        │
│  Files  │        │
└────┬────┘        │
     │             │
     ▼             │
┌─────────┐        │
│  Print  │        │
│ Ticket  │        │
└────┬────┘        │
     │             │
     ▼             │
┌─────────┐        │
│   End   │◄───────┘
└─────────┘
```

### Workflow 2: Admin Flight Management
```
┌─────────────────┐
│ Admin Login     │
└────────┬────────┘
         │
         ▼
    ┌───┴───────────┐
    │  Task Type?   │
    └───┬───────────┘
        │
   ┌────┼────┐
   │    │    │
View  Add  Delete
   │    │    │
   ▼    ▼    ▼
```

**View Flights:**
- Loads all aircraft files
- Displays consolidated schedule
- Shows availability

**Add Flight:**
1. Validate aircraft exists
2. Generate flight number
3. Initialize seat map
4. Save to aircraft CSV

**Delete Flight:**
1. Locate flight in aircraft CSV
2. Remove flight record
3. Delete passenger bookings
4. Free seat allocations

### Workflow 3: Reservation to Booking
```
Reserve Seat → Enter Details → Seat Marked 'R' → Generate PNR
                                                     ↓
     ┌───────────────────────────────────────────────┘
     │
     ▼
Later: Book Reserved
     ↓
Enter PNR → Validate → Convert 'R' to '1' → Update Status
     ↓
Print Confirmed Ticket
```

---

## 🛠️ Technical Documentation

### Code Structure

#### Console Interface (`airline_console.py`)

**Main Functions:**
```python
# Flight Management
chkflights()        # Display all flights
addflight()         # Add new flight
delflight()         # Delete flight

# Passenger Management
chkpassengers()     # View passenger details
addpassenger()      # Add passenger booking

# Schedule & Booking
schedule()          # Search flights
bookticket()        # Book ticket workflow
getticket()         # Print ticket by PNR

# Cancellation
cancelflight()      # Cancel booking

# Reservation
reserve()           # Make reservation
bookreserve()       # Confirm reservation
chkreservation()    # View reservations
cancelreservation() # Cancel reservation
```

**Global Variables:**
```python
m = datetime.datetime.now()  # Booking timestamp
maindata = []                # Temporary data storage
```

#### GUI Interface (`airline_gui.py`)

**Class Structure:**
```python
class AirlineReservationSystem:
    """Backend business logic"""
    
    def __init__(self)
    def ensure_files_exist()
    def get_aircraft_names()
    def get_flights()
    def add_flight(...)
    def delete_flight(...)
    def get_passengers(...)
    def get_schedule(...)
    def get_reservations(...)
    def get_ticket_info(...)

class AirlineGUI:
    """Main GUI application"""
    
    def __init__(self, root)
    def setup_gui()
    def setup_admin_panel()
    def setup_user_panel()
    # ... event handlers ...

class AddAircraftWindow:
    """Popup window for aircraft configuration"""
    
    def __init__(self, parent)
    def add_aircraft()
```

### Key Algorithms

#### 1. Seat Selection Algorithm
```python
# Pseudo-code
function select_seat(flight, class, row, seat_number):
    # Load flight data
    flight_data = load_flight(flight)
    
    # Get seat map for row
    seat_map = get_row_seat_map(flight_data, row)
    
    # Check availability
    if seat_map[seat_number] == '0':
        # Mark as booked
        seat_map[seat_number] = '1'
        update_seat_map(flight, row, seat_map)
        return True
    else:
        return False  # Seat not available
```

#### 2. PNR Generation
```python
# Sequential PNR starting from 10000
function generate_pnr():
    last_record = get_last_passenger_record()
    if last_record exists:
        last_pnr = last_record.pnr
        new_pnr = int(last_pnr) + 1
    else:
        new_pnr = 10000
    return new_pnr
```

#### 3. Flight Number Generation
```python
# Format: KR + sequential number
function generate_flight_number(aircraft):
    last_flight = get_last_flight(aircraft)
    if last_flight exists:
        last_number = extract_number(last_flight.number)
        new_number = last_number + 1
    else:
        new_number = 1000
    return "KR" + str(new_number)
```

### Input Validation

#### Date Validation
```python
# Day: 1-31
# Month: 1-12 (converted to Jan-Dec)
# Year: Two-digit, >= 23
```

#### Name Validation
```python
# Only alphabetic characters allowed
# Spaces allowed (first, middle, last name)
# Converted to uppercase
```

#### Phone Validation
```python
# Can start with '+' for international
# Rest must be digits
# Example: +91-9876543210
```

#### Price Validation
```python
# Must satisfy: Economy < Business < First
# All must be positive integers
```

### Error Handling

**File Operations:**
```python
try:
    with open(filename, 'r') as f:
        data = csv.reader(f)
except FileNotFoundError:
    # Create file with headers
    initialize_file(filename)
except PermissionError:
    # Show error message
    display_error("File access denied")
```

**Data Validation:**
```python
# Check all required fields
if not all([field1, field2, ...]):
    show_error("All fields required")
    return

# Validate data types
try:
    age = int(age_input)
except ValueError:
    show_error("Age must be a number")
    return
```

---

## 🐛 Troubleshooting

### Common Issues

#### Issue 1: "Aircraft not found" when adding flight

**Cause:** Aircraft doesn't exist in AIRCRAFT.CSV

**Solution:**
1. Go to Tools → Add Aircraft (GUI)
2. Or manually add to AIRCRAFT.CSV:
```csv
   AIRCRAFT_NAME,CAPACITY,ECONOMY,BUSINESS,FIRST
```

#### Issue 2: "Flight not found" when booking

**Cause:** 
- Flight doesn't exist
- Wrong flight number format

**Solution:**
- Use "View Flights" to see exact flight numbers
- Format: KR followed by number (e.g., KR1000)

#### Issue 3: Seat not available

**Causes:**
- Seat already booked (marked '1')
- Seat reserved (marked 'R')
- Class full

**Solution:**
- Choose different seat
- Check seat availability in flight list
- Try different class

#### Issue 4: PNR not found when printing ticket

**Causes:**
- Incorrect PNR number
- Booking was cancelled
- Data file corrupted

**Solution:**
- Verify PNR (5-digit number, starts with 10000)
- Check "View Passengers" to confirm booking exists
- Check PASSENGER DETAILS.CSV file

#### Issue 5: CSV file errors

**Symptoms:**
- IndexError: list index out of range
- File not found errors
- Data not displaying

**Solutions:**
1. Check CSV file format
2. Ensure headers are present
3. Verify no empty lines in middle of file
4. Check file permissions
5. Re-initialize files:
```python
   # Delete all CSV files and restart
   # System will recreate with proper headers
```

#### Issue 6: GUI not displaying data

**Cause:** CSV files have incorrect format or missing data

**Solution:**
1. Check console for error messages
2. Verify CSV file structure
3. Use "Refresh" buttons
4. Restart application

#### Issue 7: Seat map corruption

**Symptoms:** Seats showing wrong status

**Solution:**
1. Manual fix in CSV:
   - Each row should be 4 characters
   - Format: `XYZR` (X=seat1, Y=seat2, Z=seat3, R=row letter)
   - Valid values: 0, 1, R
2. Example correct format: `000A`, `110B`, `R01C`

### Debug Mode

**Enable Detailed Logging (Console):**
```python
# Add at top of functions
print(f"DEBUG: Variable name = {value}")
```

**Check File Contents:**
```python
# Quickly view CSV contents
import csv
with open('AIRCRAFT.CSV', 'r') as f:
    print(list(csv.reader(f)))
```

### Data Recovery

**Backup Strategy:**
```bash
# Before major operations, backup CSV files
cp AIRCRAFT.CSV AIRCRAFT.CSV.backup
cp *.csv backups/
```

**Restore from Backup:**
```bash
cp AIRCRAFT.CSV.backup AIRCRAFT.CSV
```

---

## 🚀 Future Enhancements

### Planned Features

#### Version 2.0
- [ ] **Database Integration**: Migrate from CSV to SQLite/PostgreSQL
- [ ] **User Authentication**: Login system with role-based access
- [ ] **Payment Integration**: Online payment gateway
- [ ] **Email Notifications**: Send tickets via email
- [ ] **SMS Alerts**: Flight reminders and updates

#### Version 2.5
- [ ] **Web Interface**: Flask/Django web application
- [ ] **Mobile App**: React Native/Flutter app
- [ ] **Real-time Updates**: WebSocket for live availability
- [ ] **Analytics Dashboard**: Booking trends and revenue reports
- [ ] **Multi-language Support**: i18n implementation

#### Version 3.0
- [ ] **AI Features**:
  - Dynamic pricing based on demand
  - Seat recommendation engine
  - Chatbot for customer support
- [ ] **Advanced Booking**:
  - Multi-city bookings
  - Group bookings
  - Frequent flyer program
- [ ] **Integration**:
  - Airport APIs
  - Weather data
  - Hotel booking
  - Car rental

### Technical Improvements

#### Code Quality
- [ ] Unit tests (pytest)
- [ ] Integration tests
- [ ] Code documentation (Sphinx)
- [ ] Type hints (mypy)
- [ ] Linting (pylint, flake8)

#### Performance
- [ ] Caching layer (Redis)
- [ ] Async operations
- [ ] Load balancing
- [ ] Connection pooling

#### Security
- [ ] Input sanitization
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF tokens
- [ ] Password hashing (bcrypt)
- [ ] SSL/TLS encryption

### UI/UX Enhancements

#### GUI Improvements
- [ ] Seat map visualization (graphical grid)
- [ ] Color-coded availability
- [ ] Flight comparison tool
- [ ] Price calendar
- [ ] Booking history
- [ ] Profile management

#### Accessibility
- [ ] Keyboard navigation
- [ ] Screen reader support
- [ ] High contrast mode
- [ ] Font size adjustment
- [ ] Multi-device responsive design

---

1
