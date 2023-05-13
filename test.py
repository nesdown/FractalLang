# Приклад бази даних макрос-команд
macro_commands = {
    "calculate_mean": {
        "module": "statistics",
        "function": "mean",
        "parameters": {
            "time_series": None
        }
    },
    "calculate_std_dev": {
        "module": "statistics",
        "function": "stdev",
        "parameters": {
            "time_series": None
        }
    },
    "plot_time_series": {
        "module": "visualization",
        "function": "plot",
        "parameters": {
            "time_series": None
        }
    }
}
