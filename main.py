import streamlit as st

def price(base_fare, modifier, fixed_fee, tax_rate):
    return base_fare + (base_fare * modifier) + fixed_fee + (base_fare * tax_rate)

# Pricing tables for different ride services
pricing_tables = {
    'Ecolite (Uber X Saver)': [
        (1, 0.6, 0.6, 0.20, 3, 0.15),
        (2, 0.6, 0.5, 0.10, 3, 0.15),
        (3, 0.7, 0.7, 0.10, 3, 0.15),
        (4, 0.5, 0.5, 0.15, 3, 0.15),
        (5, 0.5, 0.8, 0.20, 3, 0.15),
        (6, 1.0, 0.5, 0.10, 3, 0.15),
        (7, 0.5, 0.8, 0.25, 3, 0.15),
        (8, 0.5, 0.6, 0.10, 3, 0.15),
        (9, 0.6, 0.8, 0.15, 3, 0.15),
        (10, 0.6, 0.5, 0.10, 3, 0.15),
        (50, 0.82, 0.5, 0.10, 3, 0.15)
    ],
    'ECO (Uber X)': [
        (1, 1.0, 1.0, 0.50, 4, 0.15),
        (2, 0.6, 0.5, 0.50, 4, 0.15),
        (3, 0.5, 0.5, 0.10, 4, 0.15),
        (4, 0.5, 0.5, 0.10, 4, 0.15),
        (5, 0.5, 0.8, 0.10, 4, 0.15),
        (6, 0.6, 0.5, 0.25, 4, 0.15),
        (7, 0.5, 0.8, 0.25, 4, 0.15),
        (8, 0.6, 0.7, 0.10, 4, 0.15),
        (9, 0.6, 0.8, 0.10, 4, 0.15),
        (10, 0.6, 0.8, 0.10, 4, 0.15),
        (50, 1.0, 1.0, 0.10, 15, 0.15)
    ],
    'Plus (Uber XL & Comfort)': [
        (1, 1.0, 1.0, 0.50, 6, 0.15),
        (2, 0.6, 0.5, 0.50, 6, 0.15),
        (3, 0.5, 0.5, 0.10, 6, 0.15),
        (4, 0.5, 0.5, 0.10, 6, 0.15),
        (5, 0.5, 0.8, 0.10, 6, 0.15),
        (6, 0.6, 0.5, 0.25, 6, 0.15),
        (7, 0.5, 0.8, 0.25, 6, 0.15),
        (8, 0.6, 0.7, 0.10, 6, 0.15),
        (9, 0.6, 0.8, 0.10, 6, 0.15),
        (10, 0.6, 0.8, 0.10, 6, 0.15),
        (50, 1.0, 1.0, 0.15, 20, 0.15)
    ]
}

def calculate_fare(service_type, minutes, km):
    table = pricing_tables.get(service_type)
    if not table:
        return "Invalid service type"
    
    for max_km, distance_factor, minute_rate, additional_pct, fixed_fee, tax_rate in table:
        if km <= max_km:
            base_fare = (distance_factor * km) + (minute_rate * minutes)
            return price(base_fare, additional_pct, fixed_fee, tax_rate)
    
    # Use the last pricing tier if distance exceeds the maximum
    max_km, distance_factor, minute_rate, additional_pct, fixed_fee, tax_rate = table[-1]
    base_fare = (distance_factor * km) + (minute_rate * minutes)
    return price(base_fare, additional_pct, fixed_fee, tax_rate)

st.title('ARK Adaptive Pricing Engine')

mins = st.number_input('Enter Minutes:', min_value=0.0, step=0.1)
km = st.number_input('Enter Distance (KM):', min_value=0.0, step=0.1)

ride_types = ['Ecolite (Uber X Saver)', 'ECO (Uber X)', 'Plus (Uber XL & Comfort)']

if st.button('Calculate Fare'):
    fare_ecolite = calculate_fare('Ecolite (Uber X Saver)', mins, km)
    fare_eco = calculate_fare('ECO (Uber X)', mins, km)
    fare_plus = calculate_fare('Plus (Uber XL & Comfort)', mins, km)
    
    st.write(f'The fare for Ecolite is: SAR {fare_ecolite:.2f}')
    st.write(f'The fare for ECO is: SAR {fare_eco:.2f}')
    st.write(f'The fare for Plus is: SAR {fare_plus:.2f}')
