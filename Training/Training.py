import pandas
import fpdf

df = pandas.read_csv("articles.csv", dtype={'id': str})

class Buy:
    def __init__(self,article_ID):
        self.article_ID = article_ID
        self.in_stock = df.loc[df["id"] == self.article_ID, "in stock"].squeeze()

    def purchase(self):
        if self.in_stock > 0:
            df.loc[df["id"] == self.article_ID, "in stock"] = df.loc[df["id"] == self.article_ID, "in stock"] - 1
            df.to_csv("articles.csv", index=False)  # index = False, Python does not add another column
            return "in stock"
        else:
            return "not in stock"

class Reciept:
    def create_PDF(self, receipt_nr):
        pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4") # Creating PDF
        pdf.add_page() # Added page

        invoice_nr = receipt_nr
        article = df.loc[df["id"] == receipt_nr, "name"].squeeze()
        print(article)
        price = df.loc[df["id"] == receipt_nr, "price"].squeeze()
        print(price)

        # PDF Cells
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)  # ln goes to new line
        pdf.cell(w=50, h=8, txt=f"Article: {article}", ln=1)  # ln goes to new line
        pdf.cell(w=50, h=8, txt=f"Price: {price}", ln=1)  # ln goes to new line

        # Generating actual PDF
        pdf.output(f"{invoice_nr}.pdf")


print(df)
article_to_buy = input("Choose an article to buy: ")
purchase = Buy(article_to_buy)
print(purchase.purchase())

receipt = Reciept()
receipt.create_PDF(purchase.article_ID)
