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
- <code title="get /individuals/{id}">client.individuals.<a href="./src/dataleon/resources/individuals/individuals.py">retrieve</a>(id, \*\*<a href="src/dataleon/types/individual_retrieve_params.py">params</a>) -> <a href="./src/dataleon/types/individual.py">Individual</a></code>
- <code title="put /individuals/{id}">client.individuals.<a href="./src/dataleon/resources/individuals/individuals.py">update</a>(id, \*\*<a href="src/dataleon/types/individual_update_params.py">params</a>) -> <a href="./src/dataleon/types/individual.py">Individual</a></code>
- <code title="get /individuals">client.individuals.<a href="./src/dataleon/resources/individuals/individuals.py">list</a>(\*\*<a href="src/dataleon/types/individual_list_params.py">params</a>) -> <a href="./src/dataleon/types/individual_list_response.py">IndividualListResponse</a></code>
- <code title="delete /individuals/{id}">client.individuals.<a href="./src/dataleon/resources/individuals/individuals.py">delete</a>(id) -> None</code>

## Documents

Types:

```python
from dataleon.types.individuals import DocumentResponse, GenericDocument
```

Methods:

- <code title="get /individuals/{id}/documents">client.individuals.documents.<a href="./src/dataleon/resources/individuals/documents.py">list</a>(id) -> <a href="./src/dataleon/types/individuals/document_response.py">DocumentResponse</a></code>
- <code title="post /individuals/{id}/documents">client.individuals.documents.<a href="./src/dataleon/resources/individuals/documents.py">upload</a>(id, \*\*<a href="src/dataleon/types/individuals/document_upload_params.py">params</a>) -> <a href="./src/dataleon/types/individuals/generic_document.py">GenericDocument</a></code>

# Companies

Types:

```python
from dataleon.types import CompanyRegistration, CompanyListResponse
```

Methods:

- <code title="post /companies">client.companies.<a href="./src/dataleon/resources/companies/companies.py">create</a>(\*\*<a href="src/dataleon/types/company_create_params.py">params</a>) -> <a href="./src/dataleon/types/company_registration.py">CompanyRegistration</a></code>
- <code title="get /companies/{id}">client.companies.<a href="./src/dataleon/resources/companies/companies.py">retrieve</a>(id, \*\*<a href="src/dataleon/types/company_retrieve_params.py">params</a>) -> <a href="./src/dataleon/types/company_registration.py">CompanyRegistration</a></code>
- <code title="put /companies/{id}">client.companies.<a href="./src/dataleon/resources/companies/companies.py">update</a>(id, \*\*<a href="src/dataleon/types/company_update_params.py">params</a>) -> <a href="./src/dataleon/types/company_registration.py">CompanyRegistration</a></code>
- <code title="get /companies">client.companies.<a href="./src/dataleon/resources/companies/companies.py">list</a>(\*\*<a href="src/dataleon/types/company_list_params.py">params</a>) -> <a href="./src/dataleon/types/company_list_response.py">CompanyListResponse</a></code>
- <code title="delete /companies/{id}">client.companies.<a href="./src/dataleon/resources/companies/companies.py">delete</a>(id) -> None</code>

## Documents

Methods:

- <code title="get /companies/{id}/documents">client.companies.documents.<a href="./src/dataleon/resources/companies/documents.py">list</a>(id) -> <a href="./src/dataleon/types/individuals/document_response.py">DocumentResponse</a></code>
- <code title="post /companies/{id}/documents">client.companies.documents.<a href="./src/dataleon/resources/companies/documents.py">upload</a>(id, \*\*<a href="src/dataleon/types/companies/document_upload_params.py">params</a>) -> <a href="./src/dataleon/types/individuals/generic_document.py">GenericDocument</a></code>
