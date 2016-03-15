class pollsRouter(object):
    
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'Question':
            return 'questiondb'
        if model._meta.db_table == 'phpQuestion':
        	return 'phpQuestion'
        return None

    # def db_for_write(self,model, **hints):
    #    if model._meta.app_label == 'app2':
    #         return 'default'
    #     return None