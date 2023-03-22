import streamlit as st

# Define the finite state automata for the vending machine
state_transitions = {
    'start': {'coin': 'has_coin'},
    'has_coin': {'select_coke': 'dispense_coke', 'select_pepsi': 'dispense_pepsi', 'refund': 'start'},
    'dispense_coke': {'refund': 'start'},
    'dispense_pepsi': {'refund': 'start'},
}

class VendingMachine:
    def __init__(self):
        self.state = 'start'
    
    def process(self, input_symbols):
        for symbol in input_symbols:
            if symbol in state_transitions[self.state]:
                self.state = state_transitions[self.state][symbol]
            else:
                return False
        return True

# Define the Streamlit app
def main():
    # Create a new vending machine object
    vending_machine = VendingMachine()
    
    st.title('Finite State Automata Vending Machine')
    
    # Display the current state of the vending machine
    st.write(f"Current state: {vending_machine.state}")
    
    # Get input from the user
    input_symbols = st.text_input('Enter input symbols separated by commas').split(',')
    
    # Process the input and update the state of the vending machine
    if input_symbols:
        if vending_machine.process(input_symbols):
            st.write(f"Input accepted. New state: {vending_machine.state}")
        else:
            st.write(f"Input rejected. Current state: {vending_machine.state}")

if __name__ == '__main__':
    main()