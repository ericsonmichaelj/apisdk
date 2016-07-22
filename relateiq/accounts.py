from relateiq.riq_obj import RIQObject
from relateiq.riq_base import RIQBase

class Account(RIQObject,RIQBase) :
    # Object Attributes
    _id = None
    _name = None
    _modifiedDate = None
    _fieldValues = None
    def __init__(self, _id=None, name=None, modifiedDate=None, data=None, fieldValues = None) :
        if data != None :
            self.parse(data)
        elif self.id(_id) != None :
            self.get()

        self.name(name)
        self.modifiedDate(modifiedDate)
        self.fieldValues(fieldValues)

    @classmethod
    def node(cls) :
        return 'accounts'

    def parse(self,data) :
        fieldValues = {}
        for field,valueList in data.get('fieldValues',{}).items() :
            fieldValue = []
            if len(valueList) == 1 :
                fieldValue = valueList[0].get('raw',None)
            else :
                for val in valueList :
                    fieldValue.append(val.get('raw',None))
            fieldValues[field] = fieldValue
        self.fieldValues(fieldValues)
        self.id(data.get('id',None))
        self.name(data.get('name',None))
        self.modifiedDate(data.get('modifiedDate',None))
        return self

    # Data Payload
    def payload(self) :
        fieldValues = {}
        for field,value in self.fieldValues().items():
            valueList = []
            if isinstance(value, str):
                value = [value]
            for val in value:
                valueList.append({'raw': val})
            fieldValues[field] = valueList
        payload = {
            'name' : self.name(),
            'fieldValues': fieldValues
        }
        if self.id() :
            payload['id'] = self.id()
        return payload

    # Hybrid
    def id(self,value=None) :
        if value != None :
            self._id = value
        return self._id

    def modifiedDate(self,value=None) :
        if value != None :
            self._modifiedDate = value
        return self._modifiedDate

    def name(self,value=None) :
        if value != None :
            self._name = value
        return self._name

    def fieldValues(self,value=None) :
            if value != None :
                for key,val in value.items() :
                    self.fieldValue(key,val)
            return self._fieldValues or {}

    def fieldValue(self,key,value=None) :
        if self._fieldValues == None :
            self._fieldValues = {}
        if value != None :
            #value = self.list().fieldOption(value)
            self._fieldValues[key] = value
        #value = self._fieldValues.get(key,None)
        return key