from product_table import NWProducts

product_runner = NWProducts()

product_runner.df_to_sql("Products", 'Paula made some changes!')

print(product_runner.check_new_table())

