import tkinter as tk
from tkinter import ttk
import math
import datetime
from datetime import timedelta

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("800x600")
        
        # Theme colors - Modern color scheme
        self.colors = {
            'bg': '#1A1A2E',  # Dark blue background
            'fg': '#E94560',  # Bright pink text
            'button': '#16213E',  # Darker blue for buttons
            'button_fg': '#0EF6CC',  # Bright cyan for button text
            'highlight': '#FF69B4',  # Hot pink for highlights
            'border': '#4D4C7D',  # Purple for borders
            'entry_bg': '#222831',  # Darker background for entry fields
            'tab_selected': '#E94560'  # Pink for selected tabs
        }
        
        # Apply modern theme with curved borders
        self.root.configure(bg=self.colors['bg'])
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure notebook tabs
        style.configure('TNotebook', background=self.colors['bg'], borderwidth=0)
        style.configure('TNotebook.Tab', background=self.colors['button'], foreground=self.colors['button_fg'],
                        padding=[10, 5], borderwidth=0)
        style.map('TNotebook.Tab', background=[('selected', self.colors['tab_selected'])],
                  foreground=[('selected', self.colors['button_fg'])])
        
        # Configure frames and labels
        style.configure('TFrame', background=self.colors['bg'])
        style.configure('TLabelframe', background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure('TLabelframe.Label', background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure('TLabel', background=self.colors['bg'], foreground=self.colors['fg'])
        
        # Configure buttons with rounded corners
        style.configure('TButton', background=self.colors['button'], foreground=self.colors['button_fg'],
                        padding=[10, 5], borderwidth=2, relief='raised')
        style.map('TButton', background=[('active', self.colors['highlight'])])
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Calculator tab
        self.calc_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.calc_frame, text='Calculator')
        
        # Date/Time tab
        self.datetime_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.datetime_frame, text='Date/Time')
        
        # Unit Converter tab
        self.unit_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.unit_frame, text='Unit Converter')
        
        self.setup_calculator()
        self.setup_datetime()
        self.setup_unit_converter()
    
    def setup_calculator(self):
        # Modern display with custom styling
        self.display = tk.Entry(self.calc_frame, width=40, font=('Helvetica', 16),
                               bg=self.colors['entry_bg'], fg=self.colors['fg'],
                               insertbackground=self.colors['fg'], justify='right',
                               relief='flat', bd=10)
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipady=12, sticky='nsew')
        
        # Scientific Calculator Buttons
        buttons = [
            'sin', 'cos', 'tan', '(', ')',
            'sqrt', 'log', 'ln', '^', 'π',
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'DEL',
            '1', '2', '3', '-', '=',
            '0', '.', 'e', '+', '±'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click_button(x)
            btn = tk.Button(self.calc_frame, text=button, width=8, height=2,
                          command=cmd, bg=self.colors['button'],
                          fg=self.colors['button_fg'], font=('Helvetica', 12, 'bold'),
                          relief='raised', bd=0, cursor='hand2')
            btn.configure(highlightbackground=self.colors['border'], highlightthickness=1)
            btn['borderwidth'] = 0
            # Add hover effect
            btn.bind('<Enter>', lambda e, btn=btn: btn.configure(bg=self.colors['highlight']))
            btn.bind('<Leave>', lambda e, btn=btn: btn.configure(bg=self.colors['button']))
            btn.grid(row=row, column=col, padx=3, pady=3)
            col += 1
            if col > 4:
                col = 0
                row += 1
    
    def setup_datetime(self):
        # Birthday Calculator Section
        birthday_frame = ttk.LabelFrame(self.datetime_frame, text="Age Calculator", padding=10)
        birthday_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        ttk.Label(birthday_frame, text="Enter Birthday:").grid(row=0, column=0, padx=5, pady=5)
        self.birthday_entry = ttk.Entry(birthday_frame)
        self.birthday_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(birthday_frame, text="(YYYY-MM-DD)").grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(birthday_frame, text="Current Date:").grid(row=1, column=0, padx=5, pady=5)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.current_date_label = ttk.Label(birthday_frame, text=current_date)
        self.current_date_label.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(birthday_frame, text="Calculate Age",
                   command=self.calculate_age).grid(row=2, column=0, columnspan=3, pady=10)
        
        self.age_result = ttk.Label(birthday_frame, text="")
        self.age_result.grid(row=3, column=0, columnspan=3, pady=5)
        
        # Date Difference Calculator Section
        diff_frame = ttk.LabelFrame(self.datetime_frame, text="Date Difference Calculator", padding=10)
        diff_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        
        ttk.Label(diff_frame, text="Date 1:").grid(row=0, column=0, padx=5, pady=5)
        self.date1 = ttk.Entry(diff_frame)
        self.date1.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(diff_frame, text="(YYYY-MM-DD)").grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(diff_frame, text="Date 2:").grid(row=1, column=0, padx=5, pady=5)
        self.date2 = ttk.Entry(diff_frame)
        self.date2.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(diff_frame, text="(YYYY-MM-DD)").grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Button(diff_frame, text="Calculate Difference",
                   command=self.calculate_date_diff).grid(row=2, column=0, columnspan=3, pady=10)
        
        self.date_result = ttk.Label(diff_frame, text="")
        self.date_result.grid(row=3, column=0, columnspan=3, pady=5)
    
    def setup_unit_converter(self):
        # Unit conversion types and their units
        self.conversion_units = {
            'Length': {
                'km': 1000,
                'm': 1,
                'cm': 0.01,
                'mm': 0.001,
                'mile': 1609.34,
                'yard': 0.9144,
                'foot': 0.3048,
                'inch': 0.0254
            },
            'Weight': {
                'kg': 1,
                'g': 0.001,
                'mg': 0.000001,
                'lb': 0.453592,
                'oz': 0.0283495
            },
            'Temperature': {
                'Celsius': 'C',
                'Fahrenheit': 'F',
                'Kelvin': 'K'
            }
        }
        
        # Unit type selector
        ttk.Label(self.unit_frame, text="Select Category:").grid(row=0, column=0, padx=5, pady=5)
        self.unit_type = ttk.Combobox(self.unit_frame, values=list(self.conversion_units.keys()))
        self.unit_type.grid(row=0, column=1, padx=5, pady=5)
        self.unit_type.bind('<<ComboboxSelected>>', self.update_unit_options)
        
        # From unit selector
        ttk.Label(self.unit_frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
        self.from_unit = ttk.Combobox(self.unit_frame)
        self.from_unit.grid(row=1, column=1, padx=5, pady=5)
        
        # To unit selector
        ttk.Label(self.unit_frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
        self.to_unit = ttk.Combobox(self.unit_frame)
        self.to_unit.grid(row=2, column=1, padx=5, pady=5)
        
        # Value input
        ttk.Label(self.unit_frame, text="Value:").grid(row=3, column=0, padx=5, pady=5)
        self.value_input = ttk.Entry(self.unit_frame)
        self.value_input.grid(row=3, column=1, padx=5, pady=5)
        
        # Convert button
        ttk.Button(self.unit_frame, text="Convert",
                   command=self.convert_units).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Result display
        self.result_label = ttk.Label(self.unit_frame, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Set default unit type
        self.unit_type.set('Length')
        self.update_unit_options()
    
    def click_button(self, value):
        if value == '=':
            try:
                expression = self.display.get()
                expression = expression.replace('^', '**')
                expression = expression.replace('π', str(math.pi))
                expression = expression.replace('e', str(math.e))
                
                for func in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt']:
                    if func in expression:
                        if func == 'ln':
                            expression = expression.replace('ln', 'math.log')
                        elif func == 'log':
                            expression = expression.replace('log', 'math.log10')
                        else:
                            expression = expression.replace(func, f'math.{func}')
                
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
        elif value == 'DEL':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        elif value == '±':
            try:
                current = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(-current))
            except:
                pass
        else:
            self.display.insert(tk.END, value)
    
    def calculate_age(self):
        try:
            birthday = datetime.datetime.strptime(self.birthday_entry.get(), "%Y-%m-%d")
            today = datetime.datetime.now()
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
            days = (today - birthday.replace(year=today.year)).days
            
            self.age_result.config(
                text=f"Age: {age} years\n"
                     f"({(age * 12)} months or {(today - birthday).days} days)")
        except:
            self.age_result.config(text="Invalid date format. Use YYYY-MM-DD")
    
    def calculate_date_diff(self):
        try:
            date1 = datetime.datetime.strptime(self.date1.get(), "%Y-%m-%d")
            date2 = datetime.datetime.strptime(self.date2.get(), "%Y-%m-%d")
            diff = abs((date2 - date1).days)
            self.date_result.config(text=f"Difference: {diff} days\n"
                                       f"({diff/365.25:.1f} years or {diff/30.44:.1f} months)")
        except:
            self.date_result.config(text="Invalid date format. Use YYYY-MM-DD")
    
    def update_unit_options(self, event=None):
        unit_type = self.unit_type.get()
        if unit_type in self.conversion_units:
            units = list(self.conversion_units[unit_type].keys())
            self.from_unit['values'] = units
            self.to_unit['values'] = units
            self.from_unit.set(units[0])
            self.to_unit.set(units[1])
    
    def convert_units(self):
        try:
            value = float(self.value_input.get())
            unit_type = self.unit_type.get()
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            
            if unit_type == 'Temperature':
                result = self.convert_temperature(value, from_unit, to_unit)
            else:
                # Convert to base unit first
                base_value = value * self.conversion_units[unit_type][from_unit]
                # Convert from base unit to target unit
                result = base_value / self.conversion_units[unit_type][to_unit]
            
            self.result_label.config(text=f"{value} {from_unit} = {result:.4g} {to_unit}")
        except:
            self.result_label.config(text="Invalid input")
    
    def convert_temperature(self, value, from_unit, to_unit):
        # Convert to Celsius first
        if from_unit == 'Fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'Kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        
        # Convert from Celsius to target unit
        if to_unit == 'Fahrenheit':
            return (celsius * 9/5) + 32
        elif to_unit == 'Kelvin':
            return celsius + 273.15
        return celsius

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()