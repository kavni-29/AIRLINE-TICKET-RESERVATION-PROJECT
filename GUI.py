import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import csv
import datetime
import os
from pathlib import Path


class AirlineReservationSystem:
    """Backend logic for airline reservation system"""
    
    def __init__(self):
        self.booking_time = None
        self.ensure_files_exist()
    
    def ensure_files_exist(self):
        """Create necessary CSV files if they don't exist"""
        files = {
            'AIRCRAFT.CSV': [['AIRCRAFT', 'CAPACITY', 'ECONOMY', 'BUSINESS', 'FIRST CLASS']],
            'PASSENGER DETAILS.CSV': [['Fl_No', 'PNR', 'SEAT', 'FROM', 'TO', 'NAME', 'AGE', 'SEX', 'ADDRESS', 'PHONE', 'AMT', 'CLASS']],
            'RESERVATION.CSV': [['Fl_No', 'PNR', 'AIRCRAFT', 'DATE', 'FROM', 'TO', 'SEAT', 'NAME', 'AGE', 'PHONE', 'CLASS', 'FARE', 'STATUS']]
        }
        
        for filename, header in files.items():
            if not os.path.exists(filename):
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(header)
    
    def get_aircraft_names(self):
        """Get list of aircraft names"""
        names = []
        try:
            with open('AIRCRAFT.CSV', 'r') as fr:
                data = list(csv.reader(fr))
                for rec in data:
                    if rec and rec[0].isalpha() == False and rec[0] != 'AIRCRAFT':
                        names.append(rec[0])
        except FileNotFoundError:
            pass
        return names
    
    def get_flights(self):
        """Get all flights data"""
        names = self.get_aircraft_names()
        all_flights = []
        
        for name in names:
            try:
                with open(f'{name}.csv', 'r') as fr:
                    reader = csv.reader(fr)
                    flights = list(reader)
                    all_flights.extend(flights)
            except FileNotFoundError:
                pass
        
        return all_flights
    
    def add_flight(self, aircraft, day, month, year, from_place, to_place, 
                   dep_time, arr_time, amt_e, amt_b, amt_f):
        """Add a new flight"""
        # Validate aircraft exists
        with open('AIRCRAFT.CSV', 'r') as fr:
            data = list(csv.reader(fr))
            found = False
            for rec in data:
                if rec and rec[0] == aircraft:
                    found = True
                    cap = rec[1]
                    break
            
            if not found:
                return False, "Aircraft not found"
        
        # Ensure aircraft CSV exists
        aircraft_file = f'{aircraft}.csv'
        if not os.path.exists(aircraft_file):
            with open(aircraft_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Fl_No', 'AIRCRAFT', 'DAY', 'MONTH', 'YEAR', 'FROM', 'TO', 
                               'DEPARTURE', 'ARRIVAL', 'SEATS(E)', 'SEATS(B)', 'SEATS(F)', 
                               'AMT(E)', 'AMT(B)', 'AMT(F)', 'A', 'B', 'C', 'D', 'E', 'F', 
                               'G', 'H', 'I', 'J', 'K'])
        
        # Get last flight number
        with open(aircraft_file, 'r') as file:
            data = list(csv.reader(file))
            if len(data) > 1:
                lastrec = data[-1]
                reffno = lastrec[0]
                refval = reffno[2:]
                num = int(refval) + 1
            else:
                num = 1000
        
        fl_no = 'KR' + str(num)
        
        # Create record
        rec = [fl_no, aircraft, day, month, year, from_place, to_place, dep_time, arr_time,
               '0', '0', '0', amt_e, amt_b, amt_f, '000A', '000B', '000C', '000D', '000E',
               '000F', '000G', '000H', '000I', '000J', '000K']
        
        with open(aircraft_file, 'a', newline='') as fa:
            writer = csv.writer(fa)
            writer.writerow(rec)
        
        return True, f"Flight {fl_no} added successfully"
    
    def delete_flight(self, fl_no):
        """Delete a flight"""
        names = self.get_aircraft_names()
        found = False
        
        for name in names:
            try:
                with open(f'{name}.csv', 'r') as fr:
                    data = list(csv.reader(fr))
                    for rec in data:
                        if rec and rec[0] == fl_no:
                            found = True
                            data.remove(rec)
                            
                            with open(f'{name}.csv', 'w', newline='') as fw:
                                writer = csv.writer(fw)
                                writer.writerows(data)
                            break
                
                if found:
                    break
            except FileNotFoundError:
                pass
        
        if not found:
            return False, "Flight not found"
        
        # Remove passenger details
        try:
            with open('PASSENGER DETAILS.CSV', 'r') as file:
                data = list(csv.reader(file))
                original_len = len(data)
                data = [rec for rec in data if rec[0] != fl_no]
                
                with open('PASSENGER DETAILS.CSV', 'w', newline='') as fw:
                    writer = csv.writer(fw)
                    writer.writerows(data)
        except FileNotFoundError:
            pass
        
        return True, "Flight deleted successfully"
    
    def get_passengers(self, filter_type, filter_value):
        """Get passenger details with filter"""
        try:
            with open('PASSENGER DETAILS.CSV', 'r') as fr:
                data = list(csv.reader(fr))
                
            if filter_type == 'flight':
                results = [rec for rec in data if rec and rec[0] == filter_value.upper()]
            elif filter_type == 'pnr':
                results = [rec for rec in data if rec and rec[1] == filter_value]
            elif filter_type == 'name':
                results = [rec for rec in data if rec and rec[5] == filter_value.upper()]
            else:
                results = []
            
            return results
        except FileNotFoundError:
            return []
    
    def get_schedule(self, from_place, to_place):
        """Get flight schedule between two places"""
        names = self.get_aircraft_names()
        results = []
        
        for name in names:
            try:
                with open(f'{name}.csv', 'r') as fr:
                    reader = csv.reader(fr)
                    for rec in reader:
                        if rec and len(rec) > 6:
                            if rec[5] == from_place and rec[6] == to_place:
                                results.append(rec)
            except FileNotFoundError:
                pass
        
        return results
    
    def get_reservations(self, filter_type, filter_value):
        """Get reservation details"""
        try:
            with open('RESERVATION.CSV', 'r') as fr:
                data = list(csv.reader(fr))
                
            if filter_type == 'flight':
                results = [rec for rec in data if rec and rec[0] == filter_value.upper()]
            elif filter_type == 'pnr':
                results = [rec for rec in data if rec and rec[1] == filter_value]
            elif filter_type == 'name':
                results = [rec for rec in data if rec and rec[7] == filter_value.upper()]
            else:
                results = []
            
            return results
        except FileNotFoundError:
            return []
    
    def get_ticket_info(self, pnr):
        """Get ticket information by PNR"""
        try:
            with open('PASSENGER DETAILS.CSV', 'r') as file:
                data = list(csv.reader(file))
                
            for rec in data:
                if rec and rec[1] == pnr:
                    return rec
            
            return None
        except FileNotFoundError:
            return None


class AirlineGUI:
    """Main GUI Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Airline Reservation System")
        self.root.geometry("1000x700")
        
        # Initialize backend
        self.system = AirlineReservationSystem()
        
        # Setup GUI
        self.setup_gui()
    
    def setup_gui(self):
        """Setup main GUI layout"""
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Admin Tab
        self.admin_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.admin_frame, text='Admin Panel')
        self.setup_admin_panel()
        
        # User Tab
        self.user_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.user_frame, text='User Panel')
        self.setup_user_panel()
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_admin_panel(self):
        """Setup admin panel"""
        # Create sub-notebook for admin functions
        admin_notebook = ttk.Notebook(self.admin_frame)
        admin_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # View Flights
        view_flights_frame = ttk.Frame(admin_notebook)
        admin_notebook.add(view_flights_frame, text='View Flights')
        self.setup_view_flights(view_flights_frame)
        
        # Add Flight
        add_flight_frame = ttk.Frame(admin_notebook)
        admin_notebook.add(add_flight_frame, text='Add Flight')
        self.setup_add_flight(add_flight_frame)
        
        # Delete Flight
        delete_flight_frame = ttk.Frame(admin_notebook)
        admin_notebook.add(delete_flight_frame, text='Delete Flight')
        self.setup_delete_flight(delete_flight_frame)
        
        # View Passengers
        view_passengers_frame = ttk.Frame(admin_notebook)
        admin_notebook.add(view_passengers_frame, text='View Passengers')
        self.setup_view_passengers(view_passengers_frame)
        
        # View Reservations
        view_reservations_frame = ttk.Frame(admin_notebook)
        admin_notebook.add(view_reservations_frame, text='View Reservations')
        self.setup_view_reservations(view_reservations_frame)
    
    def setup_view_flights(self, parent):
        """Setup view flights tab"""
        ttk.Label(parent, text="All Flights", font=('Arial', 14, 'bold')).pack(pady=10)
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(pady=5)
        
        ttk.Button(btn_frame, text="Refresh Flights", command=self.refresh_flights).pack()
        
        # Text area for displaying flights
        self.flights_text = scrolledtext.ScrolledText(parent, height=25, width=120)
        self.flights_text.pack(padx=10, pady=10, fill='both', expand=True)
    
    def refresh_flights(self):
        """Refresh flight display"""
        self.flights_text.delete(1.0, tk.END)
        flights = self.system.get_flights()
        
        if not flights:
            self.flights_text.insert(tk.END, "No flights found.\n")
            return
        
        # Display header
        if flights:
            header = "Fl_No | Aircraft | Day | Month | Year | From | To | Departure | Arrival | Seats(E) | Seats(B) | Seats(F) | Amt(E) | Amt(B) | Amt(F)\n"
            self.flights_text.insert(tk.END, header)
            self.flights_text.insert(tk.END, "-" * 150 + "\n")
            
            for flight in flights[1:]:  # Skip header row
                if flight and len(flight) >= 15:
                    line = f"{flight[0]:8} | {flight[1]:8} | {flight[2]:3} | {flight[3]:5} | {flight[4]:4} | {flight[5]:10} | {flight[6]:10} | {flight[7]:9} | {flight[8]:7} | {flight[9]:8} | {flight[10]:8} | {flight[11]:8} | {flight[12]:6} | {flight[13]:6} | {flight[14]:6}\n"
                    self.flights_text.insert(tk.END, line)
        
        self.status_bar.config(text=f"Displayed {len(flights)-1} flights")
    
    def setup_add_flight(self, parent):
        """Setup add flight tab"""
        # Scrollable frame
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        ttk.Label(scrollable_frame, text="Add New Flight", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Form fields
        fields = [
            ("Aircraft Name:", "aircraft"),
            ("Day (1-31):", "day"),
            ("Month (1-12):", "month"),
            ("Year (yy):", "year"),
            ("From:", "from_place"),
            ("To:", "to_place"),
            ("Departure Time (HH:MM):", "dep_time"),
            ("Arrival Time (HH:MM):", "arr_time"),
            ("Economy Class Price:", "amt_e"),
            ("Business Class Price:", "amt_b"),
            ("First Class Price:", "amt_f")
        ]
        
        self.add_flight_entries = {}
        for idx, (label, key) in enumerate(fields, start=1):
            ttk.Label(scrollable_frame, text=label).grid(row=idx, column=0, sticky='e', padx=5, pady=5)
            entry = ttk.Entry(scrollable_frame, width=30)
            entry.grid(row=idx, column=1, sticky='w', padx=5, pady=5)
            self.add_flight_entries[key] = entry
        
        ttk.Button(scrollable_frame, text="Add Flight", command=self.add_flight).grid(row=len(fields)+1, column=0, columnspan=2, pady=20)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def add_flight(self):
        """Add flight handler"""
        try:
            # Get values
            aircraft = self.add_flight_entries['aircraft'].get().upper()
            day = self.add_flight_entries['day'].get()
            month_num = self.add_flight_entries['month'].get()
            year = self.add_flight_entries['year'].get()
            from_place = self.add_flight_entries['from_place'].get().title()
            to_place = self.add_flight_entries['to_place'].get().title()
            dep_time = self.add_flight_entries['dep_time'].get()
            arr_time = self.add_flight_entries['arr_time'].get()
            amt_e = self.add_flight_entries['amt_e'].get()
            amt_b = self.add_flight_entries['amt_b'].get()
            amt_f = self.add_flight_entries['amt_f'].get()
            
            # Validate
            if not all([aircraft, day, month_num, year, from_place, to_place, dep_time, arr_time, amt_e, amt_b, amt_f]):
                messagebox.showerror("Error", "All fields are required")
                return
            
            # Convert month to name
            months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            month = months[int(month_num)]
            
            # Add flight
            success, message = self.system.add_flight(aircraft, day, month, year, from_place, to_place,
                                                     dep_time, arr_time, amt_e, amt_b, amt_f)
            
            if success:
                messagebox.showinfo("Success", message)
                # Clear entries
                for entry in self.add_flight_entries.values():
                    entry.delete(0, tk.END)
                self.status_bar.config(text=message)
            else:
                messagebox.showerror("Error", message)
                self.status_bar.config(text=message)
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_bar.config(text=f"Error: {str(e)}")
    
    def setup_delete_flight(self, parent):
        """Setup delete flight tab"""
        ttk.Label(parent, text="Delete Flight", font=('Arial', 14, 'bold')).pack(pady=10)
        
        form_frame = ttk.Frame(parent)
        form_frame.pack(pady=20)
        
        ttk.Label(form_frame, text="Flight Number:").grid(row=0, column=0, padx=5, pady=5)
        self.delete_fl_no_entry = ttk.Entry(form_frame, width=30)
        self.delete_fl_no_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(form_frame, text="Delete Flight", command=self.delete_flight).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Result area
        self.delete_result_text = scrolledtext.ScrolledText(parent, height=15, width=80)
        self.delete_result_text.pack(padx=10, pady=10)
    
    def delete_flight(self):
        """Delete flight handler"""
        fl_no = self.delete_fl_no_entry.get().upper()
        
        if not fl_no:
            messagebox.showerror("Error", "Please enter a flight number")
            return
        
        success, message = self.system.delete_flight(fl_no)
        
        if success:
            messagebox.showinfo("Success", message)
            self.delete_result_text.delete(1.0, tk.END)
            self.delete_result_text.insert(tk.END, f"Flight {fl_no} has been deleted successfully.\n")
            self.delete_fl_no_entry.delete(0, tk.END)
            self.status_bar.config(text=message)
        else:
            messagebox.showerror("Error", message)
            self.delete_result_text.delete(1.0, tk.END)
            self.delete_result_text.insert(tk.END, f"Error: {message}\n")
            self.status_bar.config(text=message)
    
    def setup_view_passengers(self, parent):
        """Setup view passengers tab"""
        ttk.Label(parent, text="View Passenger Details", font=('Arial', 14, 'bold')).pack(pady=10)
        
        filter_frame = ttk.Frame(parent)
        filter_frame.pack(pady=10)
        
        ttk.Label(filter_frame, text="Filter By:").grid(row=0, column=0, padx=5)
        self.passenger_filter_type = tk.StringVar(value='flight')
        ttk.Radiobutton(filter_frame, text="Flight Number", variable=self.passenger_filter_type, value='flight').grid(row=0, column=1)
        ttk.Radiobutton(filter_frame, text="PNR", variable=self.passenger_filter_type, value='pnr').grid(row=0, column=2)
        ttk.Radiobutton(filter_frame, text="Name", variable=self.passenger_filter_type, value='name').grid(row=0, column=3)
        
        search_frame = ttk.Frame(parent)
        search_frame.pack(pady=5)
        
        ttk.Label(search_frame, text="Search Value:").grid(row=0, column=0, padx=5)
        self.passenger_search_entry = ttk.Entry(search_frame, width=30)
        self.passenger_search_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(search_frame, text="Search", command=self.search_passengers).grid(row=0, column=2, padx=5)
        
        # Results area
        self.passengers_text = scrolledtext.ScrolledText(parent, height=20, width=120)
        self.passengers_text.pack(padx=10, pady=10, fill='both', expand=True)
    
    def search_passengers(self):
        """Search passengers handler"""
        filter_type = self.passenger_filter_type.get()
        search_value = self.passenger_search_entry.get()
        
        if not search_value:
            messagebox.showerror("Error", "Please enter a search value")
            return
        
        results = self.system.get_passengers(filter_type, search_value)
        
        self.passengers_text.delete(1.0, tk.END)
        
        if not results or len(results) <= 1:
            self.passengers_text.insert(tk.END, "No passenger records found.\n")
            self.status_bar.config(text="No records found")
            return
        
        # Display header
        header = "Fl_No | PNR | Seat | From | To | Name | Age | Sex | Address | Phone | Amount | Class\n"
        self.passengers_text.insert(tk.END, header)
        self.passengers_text.insert(tk.END, "-" * 120 + "\n")
        
        for rec in results[1:] if results[0][0] == 'Fl_No' else results:
            if rec:
                line = f"{rec[0]:8} | {rec[1]:6} | {rec[2]:4} | {rec[3]:10} | {rec[4]:10} | {rec[5]:15} | {rec[6]:3} | {rec[7]:3} | {rec[8]:20} | {rec[9]:12} | {rec[10]:6} | {rec[11]:5}\n"
                self.passengers_text.insert(tk.END, line)
        
        self.status_bar.config(text=f"Found {len(results)-1 if results[0][0] == 'Fl_No' else len(results)} passenger(s)")
    
    def setup_view_reservations(self, parent):
        """Setup view reservations tab"""
        ttk.Label(parent, text="View Reservation Details", font=('Arial', 14, 'bold')).pack(pady=10)
        
        filter_frame = ttk.Frame(parent)
        filter_frame.pack(pady=10)
        
        ttk.Label(filter_frame, text="Filter By:").grid(row=0, column=0, padx=5)
        self.reservation_filter_type = tk.StringVar(value='flight')
        ttk.Radiobutton(filter_frame, text="Flight Number", variable=self.reservation_filter_type, value='flight').grid(row=0, column=1)
        ttk.Radiobutton(filter_frame, text="PNR", variable=self.reservation_filter_type, value='pnr').grid(row=0, column=2)
        ttk.Radiobutton(filter_frame, text="Name", variable=self.reservation_filter_type, value='name').grid(row=0, column=3)
        
        search_frame = ttk.Frame(parent)
        search_frame.pack(pady=5)
        
        ttk.Label(search_frame, text="Search Value:").grid(row=0, column=0, padx=5)
        self.reservation_search_entry = ttk.Entry(search_frame, width=30)
        self.reservation_search_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(search_frame, text="Search", command=self.search_reservations).grid(row=0, column=2, padx=5)
        
        # Results area
        self.reservations_text = scrolledtext.ScrolledText(parent, height=20, width=120)
        self.reservations_text.pack(padx=10, pady=10, fill='both', expand=True)
    
    def search_reservations(self):
        """Search reservations handler"""
        filter_type = self.reservation_filter_type.get()
        search_value = self.reservation_search_entry.get()
        
        if not search_value:
            messagebox.showerror("Error", "Please enter a search value")
            return
        
        results = self.system.get_reservations(filter_type, search_value)
        
        self.reservations_text.delete(1.0, tk.END)
        
        if not results or len(results) <= 1:
            self.reservations_text.insert(tk.END, "No reservation records found.\n")
            self.status_bar.config(text="No records found")
            return
        
        # Display header
        header = "Fl_No | PNR | Aircraft | Date | From | To | Seat | Name | Age | Phone | Class | Fare | Status\n"
        self.reservations_text.insert(tk.END, header)
        self.reservations_text.insert(tk.END, "-" * 120 + "\n")
        
        for rec in results[1:] if results[0][0] == 'Fl_No' else results:
            if rec and len(rec) >= 13:
                line = f"{rec[0]:8} | {rec[1]:6} | {rec[2]:8} | {rec[3]:10} | {rec[4]:10} | {rec[5]:10} | {rec[6]:4} | {rec[7]:15} | {rec[8]:3} | {rec[9]:12} | {rec[10]:5} | {rec[11]:6} | {rec[12]:9}\n"
                self.reservations_text.insert(tk.END, line)
        
        self.status_bar.config(text=f"Found {len(results)-1 if results[0][0] == 'Fl_No' else len(results)} reservation(s)")
    
    def setup_user_panel(self):
        """Setup user panel"""
        # Create sub-notebook for user functions
        user_notebook = ttk.Notebook(self.user_frame)
        user_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Check Schedule
        schedule_frame = ttk.Frame(user_notebook)
        user_notebook.add(schedule_frame, text='Flight Schedule')
        self.setup_schedule(schedule_frame)
        
        # Print Ticket
        ticket_frame = ttk.Frame(user_notebook)
        user_notebook.add(ticket_frame, text='Print Ticket')
        self.setup_print_ticket(ticket_frame)
        
        # Note: Simplified booking - full seat selection would require extensive additional code
        info_frame = ttk.Frame(user_notebook)
        user_notebook.add(info_frame, text='Info')
        self.setup_info(info_frame)
    
    def setup_schedule(self, parent):
        """Setup schedule checking tab"""
        ttk.Label(parent, text="Check Flight Schedule", font=('Arial', 14, 'bold')).pack(pady=10)
        
        form_frame = ttk.Frame(parent)
        form_frame.pack(pady=20)
        
        ttk.Label(form_frame, text="From:").grid(row=0, column=0, padx=5, pady=5)
        self.from_entry = ttk.Entry(form_frame, width=30)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(form_frame, text="To:").grid(row=1, column=0, padx=5, pady=5)
        self.to_entry = ttk.Entry(form_frame, width=30)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(form_frame, text="Search Flights", command=self.search_schedule).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Results area
        self.schedule_text = scrolledtext.ScrolledText(parent, height=20, width=120)
        self.schedule_text.pack(padx=10, pady=10, fill='both', expand=True)
    
    def search_schedule(self):
        """Search schedule handler"""
        from_place = self.from_entry.get().title()
        to_place = self.to_entry.get().title()
        
        if not from_place or not to_place:
            messagebox.showerror("Error", "Please enter both origin and destination")
            return
        
        results = self.system.get_schedule(from_place, to_place)
        
        self.schedule_text.delete(1.0, tk.END)
        
        if not results:
            self.schedule_text.insert(tk.END, f"No flights available from {from_place} to {to_place}.\n")
            self.status_bar.config(text="No flights found")
            return
        
        # Display header
        header = "Fl_No | Aircraft | Day | Month | Year | From | To | Departure | Arrival | Seats(E) | Seats(B) | Seats(F) | Amt(E) | Amt(B) | Amt(F)\n"
        self.schedule_text.insert(tk.END, header)
        self.schedule_text.insert(tk.END, "-" * 150 + "\n")
        
        for flight in results:
            if flight and len(flight) >= 15 and flight[0] != 'Fl_No':
                line = f"{flight[0]:8} | {flight[1]:8} | {flight[2]:3} | {flight[3]:5} | {flight[4]:4} | {flight[5]:10} | {flight[6]:10} | {flight[7]:9} | {flight[8]:7} | {flight[9]:8} | {flight[10]:8} | {flight[11]:8} | {flight[12]:6} | {flight[13]:6} | {flight[14]:6}\n"
                self.schedule_text.insert(tk.END, line)
        
        self.status_bar.config(text=f"Found {len(results)} flight(s)")
    
    def setup_print_ticket(self, parent):
        """Setup print ticket tab"""
        ttk.Label(parent, text="Print Ticket", font=('Arial', 14, 'bold')).pack(pady=10)
        
        form_frame = ttk.Frame(parent)
        form_frame.pack(pady=20)
        
        ttk.Label(form_frame, text="PNR Number:").grid(row=0, column=0, padx=5, pady=5)
        self.pnr_entry = ttk.Entry(form_frame, width=30)
        self.pnr_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(form_frame, text="Get Ticket", command=self.print_ticket).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Ticket display area
        self.ticket_text = scrolledtext.ScrolledText(parent, height=20, width=80)
        self.ticket_text.pack(padx=10, pady=10, fill='both', expand=True)
    
    def print_ticket(self):
        """Print ticket handler"""
        pnr = self.pnr_entry.get()
        
        if not pnr:
            messagebox.showerror("Error", "Please enter a PNR number")
            return
        
        ticket_info = self.system.get_ticket_info(pnr)
        
        self.ticket_text.delete(1.0, tk.END)
        
        if not ticket_info:
            self.ticket_text.insert(tk.END, "Passenger details not found. Please recheck the PNR number.\n")
            self.status_bar.config(text="Ticket not found")
            return
        
        # Get flight details
        fl_no = ticket_info[0]
        seat = ticket_info[2]
        from_place = ticket_info[3]
        to_place = ticket_info[4]
        name = ticket_info[5]
        amt = ticket_info[10]
        cl = ticket_info[11]
        tno = 'TN' + pnr
        
        # Find flight timing
        names = self.system.get_aircraft_names()
        deptime = arrtime = date = "N/A"
        
        for aircraft in names:
            try:
                with open(f'{aircraft}.csv', 'r') as fr:
                    reader = csv.reader(fr)
                    for rec in reader:
                        if rec and rec[0] == fl_no:
                            deptime = rec[7]
                            arrtime = rec[8]
                            date = f"{rec[2]}-{rec[3]}-{rec[4]}"
                            break
            except FileNotFoundError:
                pass
        
        # Display ticket
        now = datetime.datetime.now()
        self.ticket_text.insert(tk.END, "-" * 80 + "\n")
        self.ticket_text.insert(tk.END, f"Booked on: {now.strftime('%d/%m/%y %H:%M:%S')}\n")
        self.ticket_text.insert(tk.END, "Fly Air Airlines\n")
        self.ticket_text.insert(tk.END, "PASSENGER TICKET\n")
        self.ticket_text.insert(tk.END, "-" * 80 + "\n\n")
        self.ticket_text.insert(tk.END, f"Ticket No.:     {tno:20}  Flight No.:  {fl_no}\n")
        self.ticket_text.insert(tk.END, f"Seat:           {seat:20}  Name:        {name}\n")
        self.ticket_text.insert(tk.END, f"Date:           {date:20}  Status:      Confirmed\n")
        self.ticket_text.insert(tk.END, f"From:           {from_place:20}  To:          {to_place}\n")
        self.ticket_text.insert(tk.END, f"Departure:      {deptime:20}  Arrival:     {arrtime}\n")
        self.ticket_text.insert(tk.END, f"Class:          {cl:20}  Fare:        {amt}\n")
        self.ticket_text.insert(tk.END, "-" * 80 + "\n")
        
        self.status_bar.config(text=f"Ticket {tno} displayed")
    
    def setup_info(self, parent):
        """Setup info tab"""
        ttk.Label(parent, text="Airline Reservation System", font=('Arial', 16, 'bold')).pack(pady=20)
        
        info_text = """
        Welcome to the Airline Reservation System!
        
        ADMIN PANEL:
        - View Flights: See all available flights
        - Add Flight: Add new flight schedules
        - Delete Flight: Remove flights from the system
        - View Passengers: Check passenger booking details
        - View Reservations: Check reservation details
        
        USER PANEL:
        - Flight Schedule: Search for flights between destinations
        - Print Ticket: Retrieve and print your ticket using PNR number
        
        NOTES:
        - This is a simplified GUI version of the console application
        - Full booking functionality requires aircraft configuration in AIRCRAFT.CSV
        - Ensure CSV files are properly formatted
        - PNR numbers are automatically generated starting from 10000
        
        SETUP:
        1. Add aircraft to AIRCRAFT.CSV with format: NAME,CAPACITY,ECONOMY,BUSINESS,FIRST_CLASS
        2. Each aircraft will have its own CSV file for flight schedules
        3. Use Admin panel to add flights
        4. Users can then search and book tickets
        
        For advanced booking features (seat selection, cancellation, reservations),
        please use the original console application or extend this GUI.
        
        Version: 1.0
        © 2024 Fly Air Airlines
        """
        
        info_label = tk.Text(parent, wrap=tk.WORD, height=25, width=90)
        info_label.pack(padx=20, pady=20, fill='both', expand=True)
        info_label.insert(1.0, info_text)
        info_label.config(state='disabled')


class AddAircraftWindow:
    """Window for adding aircraft configuration"""
    
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Add Aircraft")
        self.window.geometry("400x300")
        
        ttk.Label(self.window, text="Add New Aircraft", font=('Arial', 14, 'bold')).pack(pady=10)
        
        form_frame = ttk.Frame(self.window)
        form_frame.pack(pady=20)
        
        fields = [
            ("Aircraft Name:", "name"),
            ("Total Capacity:", "capacity"),
            ("Economy Seats:", "economy"),
            ("Business Seats:", "business"),
            ("First Class Seats:", "first")
        ]
        
        self.entries = {}
        for idx, (label, key) in enumerate(fields):
            ttk.Label(form_frame, text=label).grid(row=idx, column=0, sticky='e', padx=5, pady=5)
            entry = ttk.Entry(form_frame, width=25)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            self.entries[key] = entry
        
        ttk.Button(form_frame, text="Add Aircraft", command=self.add_aircraft).grid(row=len(fields), column=0, columnspan=2, pady=20)
    
    def add_aircraft(self):
        """Add aircraft to system"""
        name = self.entries['name'].get().upper()
        capacity = self.entries['capacity'].get()
        economy = self.entries['economy'].get()
        business = self.entries['business'].get()
        first = self.entries['first'].get()
        
        if not all([name, capacity, economy, business, first]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            # Validate numbers
            int(capacity)
            int(economy)
            int(business)
            int(first)
            
            # Add to AIRCRAFT.CSV
            with open('AIRCRAFT.CSV', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, capacity, economy, business, first])
            
            # Create aircraft-specific CSV
            with open(f'{name}.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Fl_No', 'AIRCRAFT', 'DAY', 'MONTH', 'YEAR', 'FROM', 'TO', 
                               'DEPARTURE', 'ARRIVAL', 'SEATS(E)', 'SEATS(B)', 'SEATS(F)', 
                               'AMT(E)', 'AMT(B)', 'AMT(F)', 'A', 'B', 'C', 'D', 'E', 'F', 
                               'G', 'H', 'I', 'J', 'K'])
            
            messagebox.showinfo("Success", f"Aircraft {name} added successfully!")
            self.window.destroy()
        
        except ValueError:
            messagebox.showerror("Error", "Capacity and seat numbers must be integers")
        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    """Main entry point"""
    root = tk.Tk()
    
    # Add menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)
    
    # Tools menu
    tools_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Tools", menu=tools_menu)
    tools_menu.add_command(label="Add Aircraft", command=lambda: AddAircraftWindow(root))
    
    # Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", 
        "Airline Reservation System v1.0\n\nA comprehensive flight management system\n\n© 2024 Fly Air Airlines"))
    
    # Initialize GUI
    app = AirlineGUI(root)
    
    # Auto-refresh flights on startup
    root.after(500, app.refresh_flights)
    
    root.mainloop()


if __name__ == "__main__":
    main()