
def up(config, database, semester, course):
    # SQL command to add the new column
    database.execute('ALTER TABLE public.gradeable_component ADD COLUMN gc_is_curve BOOLEAN DEFAULT FALSE')

def down(config, database, semester, course):
    # SQL command to remove the new column
    database.execute('ALTER TABLE public.gradeable_component DROP COLUMN IF EXISTS gc_is_curve CASCADE')