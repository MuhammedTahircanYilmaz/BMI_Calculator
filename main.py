from tkinter import *


def calculate_bmi():

    height = height_entry.get()
    weight = weight_entry.get()

    if height == "" or weight == "":
        results_label.config(text="please enter both weight and height")
    else:
        try:
            bmi = (int(weight) / int(height)**2)*10000
            bmi = round(bmi, 1)

            if bmi < 18.5:
                results_label.config(text=f"Your Body Mass Index is {bmi}, this is considered underweight")
            elif 18.5 <= bmi < 25:
                results_label.config(text=f"Your Body Mass Index is {bmi}, this is considered normal")
            elif 25 <= bmi < 30:
                results_label.config(text=f"Your Body Mass Index is {bmi}, this is considered overweight")
            elif 30 <= bmi < 35:
                results_label.config(text=f"Your Body Mass Index is {bmi}, this is considered mildly obese")
            elif 35 <= bmi < 40:
                results_label.config(text=f"Your Body Mass Index is {bmi}, this is considered moderately obese")
            else:
                results_label.config(text=f"Your Body Mass Index is {bmi}, this is considered morbidly obese")

        except ValueError:
            results_label.config(text="Please enter valid numbers")


if __name__ == '__main__':

    # Window
    window = Tk()
    window.title("BMI Calculator")
    window.minsize(300, 250)
    window.config(padx=20, pady=10)

    # Weight Label
    weight_label = Label(text="Please enter your weight (kg)")
    weight_label.config(pady=5)
    weight_label.pack()

    # Weight Entry
    weight_entry = Entry(width=10)
    weight_entry.pack()

    # Height Label
    height_label = Label(text="Please enter your height (cm)")
    height_label.config(pady=5)
    height_label.pack()

    # Height Entry
    height_entry = Entry(width=10)
    height_entry.pack()

    # Calculation Button
    button = Button(text="Calculate", command=calculate_bmi)
    button.config(pady=5)
    button.pack()

    # Results
    results_label = Label()
    results_label.config(pady=5)
    results_label.pack()

    window.mainloop()
