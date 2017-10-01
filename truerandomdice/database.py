from peewee import SqliteDatabase, Model, CharField, BooleanField, DoesNotExist

db = SqliteDatabase('apikey.db')


class ApiKey(Model):
    key = CharField(unique=True, primary_key=True)
    verified = BooleanField(default=False)

    @staticmethod
    def get_key():
        try:
            q = ApiKey.get()
            return q
        except DoesNotExist as e:
            print('no api-key')
            return None

    @staticmethod
    def save_key(key):
        return ApiKey.create(key=key)


    @staticmethod
    def delete_key():
        q = ApiKey.delete()
        q.execute()

    @staticmethod
    def update_key_to_valid():
        g = ApiKey.get_key()
        g.verified = True
        g.save()

    class Meta:
        database = db


db.create_tables([ApiKey], safe=True)

if __name__ == '__main__':
    ApiKey.save_key('dlsls')
    ApiKey.delete_key()
