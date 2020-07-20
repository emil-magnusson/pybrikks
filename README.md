# PyBrikks
 ***pybrikks** is a wrapper for the Labs2 Brikks API written in Python*
 


## API Documentation ##
https://***your-installation***.api.brikks.com/

*Replace your-installation*
## Installing ##
Check out the latest development version with:
```bash
$ git clone https://github.com/emil-magnusson/pybrikks.git
$ cd pybrikks
```
To install dependencies run:
```bash
$ pip install -r requirements.txt
```

## Usage 
Import the library, assign your installation URL and API_KEY.
```python
    >>> import pybrikks as brikks
    >>> brikks.BASE_URI = 'https://your-installation.api.brikks.com'
    >>> brikks.API_KEY = 'YOUR_API_KEY'
```
#
**Addresses**

Retrive a access address by **id**.
```python
    >>> adr = brikks.Address(id=199)
```
You can now access multiple attributes for the address. 
```python
    >>> adr.streetName, adr.streetNumber, adr.zipCode, adr.city, adr.countryCode
    >>> ('Samplestreet', '1', '745 23', 'Stockholm', 'SE')
```
If you need access to all attributes you set extend to **True**
```python
    >>> adr = brikks.Address(id=199, extend=True)
```
You have now access to the following attributes.
```python
    >>> adr.id, adr.addedAt, adr.updatedAt, adr.streetName, adr.streetNumber, adr.streetEntrance,
    >>> adr.addressDetail, adr.zipCode, adr.city, adr.countryCode, adr.latitude, adr.longitude,
    >>> adr.externalId, adr.socket, adr.areaId, adr.firstActivationDate, adr.activationDelay,
    >>> adr.searchableInCustomerPortal, adr.status, adr.template, adr.customer_id
```
If a customer is registered at that address, you have access to the customers attributes.
```python
adr.customer.firstName, adr.customer.lastName, adr.customer.phoneNumbers, adr.customer.email
('John', 'Doe', ['073-99999999', '070-00000000'], 'example@example.com')
```
#
**Sockets**

To access sockets linked to a address you can simple iterate over **adr.socket**, ex: 
```python
    >>> for socket in adr.socket:
    >>>     socket.id, socket.socketIdentifier, socket.tag, socket.accessPoint
    >>> ('1099','SC-id-0','tag-001','172.12.0.1-0-36',)
    >>> ('3095','SC-id-32','tag-002','172.12.0.1-0-37',)
```
#
**Customers**

The same concept is applied to customers.

Retrive a customer by **id**.
```python
    >>> cust = brikks.Customer(id=299)
```
You can now access multiple attributes for the customer. 
```python
    >>> cust.id, cust.firstName, cust.lastName, cust.addedAt, cust.updatedAt,
    >>> cust.postalAddress, cust.invoiceAddress, cust.invoiceTransport, 
    >>> cust.invoiceGroup, cust.custTypeId, cust.externalId, cust.email,
    >>> cust.invoiceEmail, cust.phoneNumbers, cust.isEnterprise
```
#
**Area**, **AreaType**, **CustomerType**, 

The same concept is applied to Area, AreaType, CustomerType.

### Search

If you dont know address by id you can simple search by ex street name and city.
Results is limited to 100 adrreses. 

A wildcard character * can be added in the end.

```python
q = brikks.Search()
q.address(streetName='Stor*', streetNumber=2, city='Stockholm')
```

## License

`pybrikks` is licensed under the MIT License - see the LICENSE file for details