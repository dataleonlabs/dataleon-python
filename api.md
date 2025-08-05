# Shared Types

```python
from dataleon.types import Check
```

# Individuals

Types:

```python
from dataleon.types import Individual, IndividualListResponse
```

Methods:

- <code title="post /individuals">client.individuals.<a href="./src/dataleon/resources/individuals/individuals.py">create</a>(\*\*<a href="src/dataleon/types/individual_create_params.py">params</a>) -> <a href="./src/dataleon/types/individual.py">Individual</a></code>
- <code title="get /individuals">client.individuals.<a href="./src/dataleon/resources/individuals/individuals.py">list</a>(\*\*<a href="src/dataleon/types/individual_list_params.py">params</a>) -> <a href="./src/dataleon/types/individual_list_response.py">IndividualListResponse</a></code>

## Documents

Types:

```python
from dataleon.types.individuals import DocumentResponse, GenericDocument
```

# Companies

Types:

```python
from dataleon.types import CompanyRegistration, CompanyListResponse
```

Methods:

- <code title="post /companies">client.companies.<a href="./src/dataleon/resources/companies/companies.py">create</a>(\*\*<a href="src/dataleon/types/company_create_params.py">params</a>) -> <a href="./src/dataleon/types/company_registration.py">CompanyRegistration</a></code>
- <code title="get /companies">client.companies.<a href="./src/dataleon/resources/companies/companies.py">list</a>(\*\*<a href="src/dataleon/types/company_list_params.py">params</a>) -> <a href="./src/dataleon/types/company_list_response.py">CompanyListResponse</a></code>
