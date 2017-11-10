# Ninja Web Framework v0.3.1

This is a Web Framework for a Spyware - NinjaLS - I developed for Ethical Hacking and Penetration Testing purposes. This tool was built with information-privacy responsibility in mind and its meant to be used on machines that the attacker has permission to conduct penetration testing or any other forms of information security testing. I will not be held liable for any deviations and usage of this tool for criminal purposes. 

This framework utilizes the HTTP protocol to receive data (Keystrokes, Mouse Clicks, User Activity, Images, Screenshots) from the NinjaLS Spyware tool and curates them into a dashboard where the attacker/penetration tester can sieve through the vast amount of data to get the interesting ones (e.g. those tagged with Login tags)

This has been deployed on the Amazon Cloud so it can be accessed from anywhere, anytime.

*This project is done while learning about MongoDB, AngularJS and Django and is the first time I am using these frameworks. Also, because this is built in 5 days (including improvements made to NinjaLS), there may be some inconsistencies or places where is may seem amateurish.*

Please visit my [Blog](https://www.reversethatshell.com) for more information and screenshots of this Web Framework.
- [Blog - NinjaLS Web Framwork](https://www.reversethatshell.com/2017/07/23/keylogger-and-analysis-console-penetration-testing-tool/)
- [Blog - NinjaLS Spyware Tool](https://www.reversethatshell.com/2017/07/23/keylogger-and-analysis-console-penetration-testing-tool/)

## Getting Started

These set of instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

*To be implemented once the build is stable*

### Prerequisites

**For Local Development**

This framework needs a Virtual Environment (I used Elastic Beanstalk Virtual Development Environment - eb-virt)
- Django==1.9.12
- pymongo==3.5.0
- psycopg2==2.7.3
- djangorestframework==3.6.4
- django-rest-framework-mongoengine==3.3.1
- raven==6.1.0
- cloudinary==1.8.0

### Installing

*To be implemented once the build is stable*

## Deployment

*To be implemented once the build is stable*

## Built With

* [AngularJS](https://angularjs.org/) - The Web Framework used
* [Django](https://www.djangoproject.com/) - Backend Rest API
* [MongoDB](https://www.mongodb.com/) - Database
* [Cloudinary](https://cloudinary.com/) - Image/File Management Cloud
* [Amazon Web Services](https://aws.amazon.com) - Cloud Server Hosting

## Contributing

*To be implemented once the build is stable*

## Versioning

This built is current on v0.3.x as of 10th November 2017

## Future Improvements

This sections shows the future improvements and enhancements that are planned for this tool.
* Graphical Analytics of User Activity
* Working Variables (e.g. Screenshot Threshold) for NinjaLS Spyware Tool remotely
* Examine each packet in detail just like the [NinjaLS Decryption and Analysis Tool](https://www.reversethatshell.com/2017/07/23/keylogger-and-analysis-console-penetration-testing-tool/)
* Search Images with Tag
* Using [Amazon Rekognition](https://aws.amazon.com/rekognition/) to Tag Images Automatically

## Authors

* **Chong Jin Wei** - [ReverseThatShell.com](https://www.reversethatshell.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/jinwei908/NinjaWebFramework-public/blob/master/LICENSE) file for details