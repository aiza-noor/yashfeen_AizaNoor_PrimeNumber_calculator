import streamlit as st

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    st.title("Prime Number Checker")

    number = st.number_input("Enter a number:")

    if st.button("Check"):
        if is_prime(number):
            st.write(f"{number} is a prime number.")
        else:
            st.write(f"{number} is a composite number.")

if __name__ == "__main__":
    main()
