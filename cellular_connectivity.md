## TL;DR;

Walter's modem supports two cellular technologies:
 - LTE Cat-M1 or LTE-M
 - LTE Cat-NB1/NB2 or NB-IoT

Both technologies were introduced in 4G with 3GPP rel. 13 and belong to the
LPWAN (*Long Range Wide Area Network*) family of protocols. These protocols are
designed to consume little power and have a long range. Very important is that
both of these cellular protocols are also available in 5G which ensures that
Walter is going to be able to connect when providers switch of their 4G 
infrastructure.

Many 'consumer' SIM cards do not offer access to these cellular IoT networks and
it is therefore important for you to check if your SIM card supports LTE-M or 
NB-IoT.

## No SIM card lock

Walter is absolutely SIM lock free. This means that you get absolute freedom
over which provider you are using.

## The Soracom SIM card

DPTechnics has teamed up with Soracom to be able to provide anyone, also private
individuals, with an IoT SIM card that supports both LTE Cat-M1 and LTE
Cat-NB1/NB2. The SIM cards can be ordered via the
[DPTechnics web shop](https://shop.dptechnics.com/).

Before choosing a SIM card it is important to check coverage as roaming 
agreements for cellular IoT is still an ongoing process, especially NB-IoT 
roaming is still in development. As the availability gets better every day,
Soracom keeps track of coverage with eDRX and PSM availability in a 
[Github repository](https://github.com/soracom/coverage-tests/blob/main/SORACOM-LPWAN-with-features.csv). 

## Consumer cards that support LTE-M

In 3GPP release 13 it is not possible for providers to check if an incoming 
connection is LTE Cat-M1 or another version (cat 1bis, cat 1, cat 4, ...). The
MNO (*Mobile Network Operator*) can only see this after the device has
connected. It is therefore sometimes possible to connect to LTE-M using a normal
SIM card although some providers also allow NB-IoT connectivity. Based on tests
done by users of Walter we have confirmed that the following cards are working:

|       Country       |     Provider     | Radio Access Technology |
|:-------------------:|:----------------:|:-----------------------:|
| Belgium             | Orange           | LTE-M                   |
| Belgium             | Hey!             | LTE-M                   |
| Swiss Confederation | Digital Republic | LTE-M                   |
| Australia           | Telstra Prepaid  | NB-IoT                  |
| Finland             | Elisa Prepaid    | LTE-M                   |

Please note than in the above cases eDRX and PSM are almost never available.