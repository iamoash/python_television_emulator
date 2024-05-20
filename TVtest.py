from TV import TV
import PySimpleGUI as sg

# Define TVTest
def TVtest():
    # Insert theme
    sg.theme('LightBlue')

    # Create two objects
    tv1 = TV()
    tv2 = TV()

    # Turns the tv1 and set its channel and volume to
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    # Turns the tv2 and sets its channel and volume to 
    tv2.turnOn()
    tv2.setChannel(3)
    tv2.setVolume(2)
    
    TestTV = 'TV'

    # TEST TV
    TestTV_layout = [
        [sg.Text(TestTV.center(50), font=('Lovelo', 25), justification='center')],
        [sg.Frame('', [[sg.Text(f"TV1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}.", size=(35,1), font=('Times New Roman',12))]], background_color='White',border_width=3)],
        [sg.Frame('', [[sg.Text(f"TV2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}.", size=(35,1), font=('Times New Roman',12))]], background_color='White',border_width=3)]
    ]
    
    #TestTV window
    TestTV_window = sg.Window('Test Driver Program', TestTV_layout, size=(400, 150))
    
    # Read and close window
    TestTV_window.read()
    TestTV_window.close()

if __name__ == '__main__':
    TVtest()