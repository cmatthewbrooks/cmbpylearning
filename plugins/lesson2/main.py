from app import MyTestPluginApplication
from hello import HelloWorldPrinter
from aloha import AlohaWorldPrinter


if __name__ == '__main__':

    app = MyTestPluginApplication(plugins=[HelloWorldPrinter()])
    app.run()

    app = MyTestPluginApplication(plugins=[AlohaWorldPrinter()])
    app.run()

    app = MyTestPluginApplication(plugins=[HelloWorldPrinter(), AlohaWorldPrinter()])
    app.run()
