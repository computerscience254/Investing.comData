# Investing.comData
[![HitCount](http://hits.dwyl.io/0x6f736f646f/InvestingcomData.svg)](http://hits.dwyl.io/0x6f736f646f/InvestingcomData)
![GitHub repo size](https://img.shields.io/github/repo-size/0x6f736f646f/Investing.comData?color=purple)
![GitHub language count](https://img.shields.io/github/languages/count/0x6f736f646f/Investing.comData)
![GitHub](https://img.shields.io/github/license/0x6f736f646f/Investing.comData)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Flask)
![GitHub last commit](https://img.shields.io/github/last-commit/0x6f736f646f/Investing.comData)

API for serving Opensource Data for investing.com

## Getting started
These instructions will get you a copy of the code up and running on your local host for development andd testing purposes

## Prerequisites
Things you will need to bring the project up on your local machine
```
Docker
Python3
```

## Installing Requirements
Use virtualenv and install packages

```shell
mkdir Investing
cd Investing
virtualenv --no-site-packages venv
.venv/Scripts/activate
git clone https://github.com/0x6f736f646f/Investing.comData.git
cd Investing.comData
pip install -r requirements.txt
```

## Running Flask Server
Go to the root directory and run

```python
python app.py
```

## Testing GraphQL
Go to http://localhost:5000/graphql to try GraphQL. Below are the example queries for adding a new company, getting all companies and adding new company historical data.

### Adding new company
```json
mutation {
  createCompany(name:"Safaricom"){
    company{
      name,
      id
    }
  }
}
```

### Adding new comapny historical data
```json
mutation {
  createData(date: "Aug 21, 2019", price: 10.65, openPrice: 10.70, high: 10.70, low: 10.60, vol: "757.60K", name: "Safaricom") {
    historicalData{
      date,
      price,
      vol,
      name{
        name
      }
    }
  }
}
```

### Getting a list of all companies
```json
query{
  allCompanies{
    edges{
      node{
        name,
        id,
        data{
          edges{
            node{
              date,
              price,
              vol
            }
          }
        }
      }
    }
  }
}
```

### Getting all companies historical data
```json
query {
  allData{
    edges{
      node{
        name{
          name
        },
        vol,
        openPrice,
        high,
        low,
        date
      }
    }
  }
}
```

## To-do
- [x] Laying foundation to our concepts and code
- [x] Writing GRAPHQL endpoints
- [ ] Adding Authentication and more mutations on our GRAPHQL endpoint
- [ ] Documentation
- [ ] Deploying to cloud
- [ ] Writing REST API

## Contributing

1. Fork it (<https://github.com/0x6f736f646f/Investing.comData>)
2. Clone your own fork (`git clone https://github.com/{your username}/Investing.comData.git`)
3. Change your directory (`cd Investing.comData`)
4. Create a branch to hold your development changes (`git checkout -b feature/fooBar`)
5. Commit your changes (`git commit -am 'Add some fooBar'`)
6. Push to the branch (`git push -u origin feature/fooBar`)
7. Create a new Pull Request. Folow this [instructions](https://help.github.com/articles/creating-a-pull-request-from-a-fork)


## Built With
* [Docker](https://www.docker.com/) - Container development tool
* [Flask](https://maven.apache.org/) - The web framework used
* [Heroku](https://www.heroku.com/) - Platform

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
