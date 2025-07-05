from win10toast import ToastNotifier

notifier = ToastNotifier()

def send_alert_notification(title, message):
    try:
        notifier.show_toast(
            title,
            message,
            duration=10,
            threaded=True
        )
        return {"Notification sent": True}
    except Exception as e:
        return {"Notification sent": False, "error": str(e)}
