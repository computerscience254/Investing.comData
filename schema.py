import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Company, HistoricalData, db_session

class CompanyObject(SQLAlchemyObjectType):
    class Meta:
        model = Company
        interfaces = (graphene.relay.Node, )

class CompanyConnection(graphene.relay.Connection):
    class Meta:
        node = CompanyObject

class HistoricalDataObject(SQLAlchemyObjectType):
    class Meta:
        model = HistoricalData
        interfaces = (graphene.relay.Node, )

class HistoricalDataConnection(graphene.relay.Connection):
    class Meta:
        node = HistoricalDataObject

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    # Node one object
    all_companies = SQLAlchemyConnectionField(CompanyObject)
    all_data = SQLAlchemyConnectionField(HistoricalDataObject)
    find_company = graphene.Field(lambda: CompanyObject, name=graphene.String())

    def resolve_find_user(self, args, context, info):
        query = CompanyObject.get_query(context)
        name = args.get('name')
        return query.filter(Company.name == name).first()

class CreateCompany(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    company = graphene.Field(lambda: CompanyObject)

    def mutate(self, info, name):
        company_obj = Company(name=name)
        db_session.add(company_obj)
        db_session.commit()
        return CreateCompany(company=company_obj)

class CreateData(graphene.Mutation):
    class Arguments:
        date = graphene.String(required=True)
        price = graphene.Float(required=True)
        open_price = graphene.Float(required=True)
        high = graphene.Float(required=True)
        low = graphene.Float(required=True)
        vol = graphene.String(required=True)
        name = graphene.String(required=True)

    historical_data = graphene.Field(lambda: HistoricalDataObject)

    def mutate(self, info, date, price, open_price, high, low, vol, name):
        company = Company.query.filter_by(name=name).first()
        historical_data = HistoricalData(date=date, price=price, open_price=open_price, high=high, low=low, vol=vol)
        if company is not None:
            historical_data.name = company
        db_session.add(historical_data)
        db_session.commit()
        return CreateData(historical_data=historical_data)

class Mutation(graphene.ObjectType):
    create_company = CreateCompany.Field()
    create_data = CreateData.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
