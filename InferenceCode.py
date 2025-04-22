import streamlit as st
import pickle
import numpy as np

def call_predict(data):
    with open("BestModel.pkl", 'rb') as file :
        model = pickle.load(file)

    data.pop("booking_id", None)
    input_array = np.array(list(data.values())).reshape(1,-1)
    prediction = model.predict(input_array)
    return prediction

def main():
    st.title("Hotel's Booking Status Prediction")
    st.markdown("## Welcome!")
    st.markdown("#### This web-based prediction application aims to help you in order to create a classification prediction whether the customer will continue or cancel on their hotel's booking")
    st.markdown("\n")
    st.markdown("###### Please input all of the customer data that you have on the following box, make sure that **all data is valid and not empty**")
    
    booking_id = st.text_input("Booking ID:")
    no_of_children = st.number_input("Number of Children:", step = 1)
    no_of_adults = st.number_input("Number of Adults:", step = 1)
    no_of_weekend_nights = st.number_input("Number of Customer's Nights on Weekend:", step = 1)
    no_of_week_nights = st.number_input("Number of Customer's Nights on Weekday:", step = 1)
    
    type_of_meal_plan_selection = {
        'Prefer to Not Selected any Meal Plan' : 0, 
        'Meal Plan 1' : 1, 
        'Meal Plan 2' : 2, 
        'Meal Plan 3' : 3
    }
    type_of_meal_plan = st.radio("What type of meal does customer prefer?", list(type_of_meal_plan_selection.keys()))
        
    required_car_parking_space_selection = {
        "Yes" : 1,
        "No" : 0
    }
    required_car_parking_space = st.radio("Does the customer need car parking space?", list(required_car_parking_space_selection.keys()))
    
    room_type_reserved_selection = {
        'Type 1' : 1, 
        'Type 2' : 2, 
        'Type 3' : 3, 
        'Type 4' : 4, 
        'Type 5' : 5, 
        'Type 6' : 6, 
        'Type 7' : 7}
    room_type_reserved = st.radio("What the type of room that customer's pick?", list(room_type_reserved_selection.keys()))
    
    lead_time = st.number_input("Number of Days between Booking Date and Arrival Date", step = 1)
    arrival_year = st.number_input("Arrival Year:", step = 1)
    arrival_month = st.slider("Arrival Month:",1,12)
    arrival_date = st.slider("Arrival Date:",1,31)
    
    market_segment_type_selection = {
        'Online' : 1, 
        'Offline' : 2, 
        'Corporate' : 3, 
        'Complementary' : 4, 
        'Aviation' : 5
    }
    market_segment_type = st.radio("The Segmentation of The Market", list(market_segment_type_selection.keys()))
    
    repeated_guest_selection = {
        "Yes" : 1,
        "No" : 0
    }
    repeated_guest = st.radio("Is the customer is the previous customer and had been stayed over the night?", list(repeated_guest_selection.keys()))
    
    no_of_previous_cancellations = st.number_input("Number of booking that had been cancelled by customer", step = 1)
    no_of_previous_bookings_not_canceled = st.number_input("Number of booking that had not been cancelled by customer", step = 1)
    avg_price_per_room = st.number_input("Room Price for One Night (in EURO)")
    no_of_special_requests = st.number_input("The number of special requests from the customer", step = 1)


    if st.button("Submit Your Data"):

        input_data = {
            "booking_id" : booking_id,
            "no_of_adults": no_of_adults,
            "no_of_children": no_of_children,
            "no_of_weekend_nights": no_of_weekend_nights,
            "no_of_week_nights": no_of_week_nights,
            "type_of_meal_plan": type_of_meal_plan_selection[type_of_meal_plan],
            "required_car_parking_space": required_car_parking_space_selection[required_car_parking_space],
            "room_type_reserved": room_type_reserved_selection[room_type_reserved],
            "lead_time": lead_time,
            "arrival_year": arrival_year,
            "arrival_month": arrival_month,
            "arrival_date": arrival_date,
            "market_segment_type": market_segment_type_selection[market_segment_type],
            "repeated_guest": repeated_guest_selection[repeated_guest],
            "no_of_previous_cancellations": no_of_previous_cancellations,
            "no_of_previous_bookings_not_canceled": no_of_previous_bookings_not_canceled,
            "avg_price_per_room": avg_price_per_room,
            "no_of_special_requests": no_of_special_requests
        }

        error_flag = False
        for key, val in input_data.items():
            if val == '' or val is None:
                st.error(f"{key.replace('_', ' ').title()} cannot be empty!")
                error_flag = True
            elif isinstance(val, (int, float)) and val < 0:
                st.error(f"{key.replace('_', ' ').title()} cannot be negative value!")
                error_flag = True
        
        if not error_flag:
            with st.spinner("Calculating the Prediction..."):
                prediction = call_predict(input_data)
            if prediction == 0:
                st.error("Oh no, The customer is possible to cancel the booking!")
            else:
                st.success("Yeay! The customer will not cancel this booking")

if __name__ == "__main__":
    main()
