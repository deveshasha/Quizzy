class pollsRouter(object):
    
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'Question':
            return 'questiondb'
        if model._meta.db_table == 'phpQuestion':
        	return 'phpQuestion'
        # if model._meta.db_table == 'userprof':
        #     return 'questiondb'
        return None

    def db_for_write(self,model, **hints):
        if model._meta.db_table == 'Question':
            return 'questiondb'
        if model._meta.db_table == 'phpQuestion':
            return 'phpQuestion'
        return None