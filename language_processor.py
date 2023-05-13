import box_counting as BC
import fourier as F
import hurst_forecasting as HF
import fbm_forecast as FBM
import mse as MSE

language_commands = ["apply analyze boxCounter", "apply analyze fourier", "apply analyze hurst", "apply forecast FBM", "apply forecast MSE"]

def language_processor (text_input):
    try: 
        if language_commands[0] in text_input:
            result = BC.run_BC()
            return result[1] 
        elif language_commands[1] in text_input:
            result = F.run_FR()
            return result[1]
        
        elif language_commands[2] in text_input:
            result = HF.run_H()
            return result[1]
        
        elif language_commands[3] in text_input:
            result = FBM.run_FMB()
            return result[1]
        
        elif language_commands[4] in text_input:
            result = MSE.run_MSE()
            return result[1]


    except Exception as e:
        return "An exception happened: " + str(e) 
