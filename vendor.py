import streamlit as st

# Define the finite state automata for the vending machine
state_transitions = {
    'start': {'coin': 'has_coin'},
    'has_coin': {'select_coke': 'dispense_coke', 'select_pepsi': 'dispense_pepsi', 'refund': 'start'},
    'dispense_coke': {'refund': 'start', 'empty_stock': 'out_of_stock'},
    'dispense_pepsi': {'refund': 'start', 'empty_stock': 'out_of_stock'},
    'out_of_stock': {'coin': 'has_coin'},
}

class VendingMachine:
    def __init__(self):
        self.state = 'start'
        self.stock = {'coke': 5, 'pepsi': 5}
    
    def process(self, input_symbols):
        for symbol in input_symbols:
            if symbol in state_transitions[self.state]:
                if symbol == 'select_coke':
                    if self.stock['coke'] > 0:
                        self.stock['coke'] -= 1
                    else:
                        self.state = 'empty_stock'
                        return True
                elif symbol == 'select_pepsi':
                    if self.stock['pepsi'] > 0:
                        self.stock['pepsi'] -= 1
                    else:
                        self.state = 'empty_stock'
                        return True
                self.state = state_transitions[self.state][symbol]
            else:
                return False
        return True

# Define the Streamlit app
def main():
    # Create a new vending machine object
    vending_machine = VendingMachine()
    
    st.title('Finite State Automata Vending Machine')
    
    # Display the current state of the vending machine and the stock
    st.write(f"Current state: {vending_machine.state}")
    st.write(f"Coke stock: {vending_machine.stock['coke']}")
    st.write(f"Pepsi stock: {vending_machine.stock['pepsi']}")
    
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
