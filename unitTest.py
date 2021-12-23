import re
from datetime import datetime

testStr = "SELECT * FROM TABLE WHERE AAA_1 = :AAA_1 AND BBB_1 = ::BBB_1, AND CCC_1 = :AAA_1 and NOW()::timestamp"
#pattern = re.compile(":\w+")
pattern = re.compile("[:]\w+")

findList = pattern.findall(testStr)
print(findList)

newFindList = []
for unit in findList :
    if unit not in newFindList and unit.upper() not in [':TIMESTAMP', ':INTERVAL']:
        newFindList.append(unit)
        #toUnit = '%(' + unit[1:] + ')s'
        toUnit = '%%(%s)s' %unit[1:]        
        testStr = testStr.replace(unit, toUnit)
print(newFindList)

print(testStr)


current = datetime.now().strftime("%Y%m%d%H%M%S")
print(current)
print(current[0:12])


from datetime import datetime
from pydantic import BaseModel, validator

class TimeModel(BaseModel):
    time: datetime

    # class Config:
    #     json_encoders = {
    #         datetime: lambda v: v.isoformat(),
    #     }

    @validator('time', pre=True)
    def time_validate(cls, v):
        print('time_validate()')
        return datetime.strptime(v, '%Y%m%d%H%M%S')


message = '{"time":"20210616104401"}'
model = TimeModel.parse_raw(message)
print(model.json())


section = 'PUSH_DATA'
if section != '':
    print('section is %s' %section)



