import platform
import dhooks

WebhookUrl = "https://discord.com/api/webhooks/969961705482366997/gZw9FLVvBDULqmoKVMN0hTStpeZovUFsMlU-mIqDI04OEXmEx1pGt36Sc29QYLnlDnVU"

dhooks.Webhook(WebhookUrl).send("Neue Sebo-Dos Installation auf " + platform.system() + "-" + platform.machine())