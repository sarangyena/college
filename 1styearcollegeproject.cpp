#include<iostream>
#include<ctime>
using namespace std;

main()
{
	//Case 1
    int trans, ndl, qty1=0, qty2=0, qty3=0, qty4=0, qty5=0, qty6=0, qty7=0, qty8=0, qty9=0, pay;
    int tothnsndl=0, totsnsndl=0, totthnsndl=0, totbill=0, change=0, totchindl=0;
    int totbeefndl=0, totporkndl=0,tothcframen=0, totsbframen=0, totcframen=0;
    
    //Case 2
    int trans2, mt, mqty1=0, mqty2=0, mqty3=0, mqty4=0, mqty5=0, mqty6=0, mqty7=0, mqty8=0, mqty9=0;
    int totbaconmt=0, tothammt=0, totchopmt=0, totchuckmt=0;
    int totgroundmt=0, totstripmt=0,totwingmt=0, totthighmt=0, totbreastmt=0;
    
    //Case 3
    int ds, dqty1=0, dqty2=0, dqty3=0, dqty4=0, dqty5=0, dqty6=0, dqty7=0, dqty8=0, dqty9=0;
    int totsjlemon=0, totsjcitrus=0, totsjbberry=0, totlemonj=0, totorangej=0, totapplej=0, totcoke=0, tot7up=0, totpepsi=0;

	string name;

    cout<<"        ___________________________________________________\n";
    cout<<"\n             Annyeong, Welcome to ABDF Korean Store!\n";
    cout<<"        ---------------------------------------------------\n";
    cout<<"Enter Costumer Name: ";
    cin>>name;
do{
	do{
    cout<<"\n           Choose what to buy below\n";
    cout<<"\n   1. Noodles";
    cout<<"\n   2. Meat";
    cout<<"\n   3. Drinks";
    cout<<"\n   4. Payment";
    cout<<"\n   Choose category [1-4]:";
    cin>>trans;
    if(trans>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"           Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
		}while (trans>4);
        switch(trans){
    case 1:{
    do {
    	do{
        cout<<"\n   1. Spicy Noodles";
        cout<<"\n   2. Flavored Noodles";
        cout<<"\n   3. Ramen";
        cout<<"\n   Choose your preferred[1-3]:";
        cin>>ndl;
        if(ndl>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"           Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
    }while (ndl>4);
    switch(ndl){
        case 1:{
            do{
            cout<<"\n      Spicy Noodles";
            cout<<"\n      1. Hot and Spicy Noodles - P 58.00";
            cout<<"\n      2. Sweet and Spicy Noodles - P 65.00";
            cout<<"\n      3. Triple Hot and Spicy Noodles - P 65.00";
            cout<<"\n      4. Return";
            cout<<"\n    Choose your preferred[1-4]:";
              cin>>ndl;
              if(ndl>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
                    switch(ndl)
                    {case 1: cout<<"  How Many Hot and Spicy Noodles? = ";
                        cin>> qty1;
                        tothnsndl= tothnsndl +(qty1 * 58);
                        cout<<"Updated Bill for Hot and Spicy Noodles = "<<tothnsndl << "\n"; break;
                    case 2: cout<<"  How Many Sweet and Spicy Noodles? = ";
                             cin>> qty2;
                        totsnsndl= totsnsndl+(qty2 * 65);
                        cout<<"Updated Bill for Sweet and Spicy Noodles = "<<totsnsndl << "\n"; break;
                     case 3: cout<<"  How Many Triple Hot and Spicy Noodles? = ";
                             cin>> qty3;
                        totthnsndl=totthnsndl +(qty3 * 65);
                        cout<<"Updated  Bill for Triple Hot and Spicy Noodles = "<<totthnsndl << "\n"; break;
                    }
               }
                while (ndl<=3);
                break;
                }
            case 2:{
            do{
            cout<<"\n      Flavored Noodles";
            cout<<"\n      1. Chicken Noodles - P 50.00";
            cout<<"\n      2. Beef Noodles - P 55.00";
            cout<<"\n      3. Pork Noodles - P 55.00";
            cout<<"\n      4. Return";
              cout<<"\n    Choose your preferred[1-4]:";
              cin>>ndl;
              if(ndl>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
                    switch(ndl)
                    {case 1: cout<<"  How Many Chicken Noodles? = ";
                        cin>> qty4;
                        totchindl= totchindl +(qty4 * 50);
                        cout<<"Updated Bill for Chicken Noodles = "<<totchindl << "\n"; break;
                    case 2: cout<<"  How Many Beef Noodles? = ";
                             cin>> qty5;
                        totbeefndl= totbeefndl+(qty5 * 55);
                        cout<<"Updated Bill for Beef Noodles = "<<totbeefndl << "\n"; break;
                     case 3: cout<<"  How Many Pork Noodles? = ";
                             cin>> qty6;
                        totporkndl=totporkndl +(qty6 * 55);
                        cout<<"Updated Bill for Pork Noodles = "<<totporkndl << "\n"; break;

                    }
               }
                while (ndl<=3);
                break;
                }
            case 3:{
            do{
            cout<<"\n      Ramen";
            cout<<"\n      1. Hot Chicken Flavor Ramen - P 70.00";
            cout<<"\n      2. Spicy Barbecue Flavor Ramen - P 75.00";
            cout<<"\n      3. Cheese Flavor Ramen - P 75.00";
            cout<<"\n      4. Return";
              cout<<"\n    Choose your preferred[1-4]:";
              cin>>ndl;
              if(ndl>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
                    switch(ndl)
                    {case 1: cout<<"  How Many Hot Chicken Flavor Ramen? = ";
                        cin>> qty7;
                        tothcframen= tothcframen +(qty7 * 70);
                        cout<<"Updated Bill for Hot Chicken Flavor Ramen = "<<tothcframen << "\n"; break;
                    case 2: cout<<"  How Many Spicy Barbecue Flavor Ramen? = ";
                             cin>> qty8;
                        totsbframen= totsbframen+(qty8 * 75);
                        cout<<"Updated  Bill for Spicy Barbecue Flavor Ramen = "<<totsbframen << "\n"; break;
                     case 3: cout<<"  How Many Cheese Flavor Ramen? = ";
                             cin>> qty9;
                        totcframen=totcframen +(qty9 * 75);
                        cout<<"Updated Bill for Cheese Flavor Ramen = "<<totcframen << "\n"; break;

                    }
               }
                while (ndl<=3);
                break;
                //default: cout<<"\n Thank you please come again!\n\n";
                }
                        }
        }
    while (ndl<=3);
    break;}
    		case 2:{//2*
    do {
    	do{
        cout<<"\n   1. Pork";
        cout<<"\n   2. Beef";
        cout<<"\n   3. Chicken";
        cout<<"\n   Choose your preferred[1-3]:";
        cin>>mt;
        if(mt>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
    }while (mt>4);
     switch(mt){
        case 1:{ //2*
            do{
            cout<<"\n      Pork";
            cout<<"\n      1. Bacon (per pack) - P130.00 ";
            cout<<"\n      2. Ham Slice (per pack) - P80.00 ";
            cout<<"\n      3. Pork Chop (per kilo) - P450.00 ";
            cout<<"\n      4. Return";
              cout<<"\n    Choose your preferred[1-4]:";
              cin>>mt;
              if(mt>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
              		switch(mt)
                    {case 1: cout<<"  How Many Packs of Bacon? = ";
                        cin>> mqty1;
                        totbaconmt= totbaconmt +(mqty1 * 130);
                        cout<<"Updated Bill for Bacon (per pack) = "<<totbaconmt << "\n"; break;
                    case 2: cout<<"  How Many Packs of Ham Slice? = ";
                             cin>> mqty2;
                        tothammt= tothammt+(mqty2 * 80);
                        cout<<"Updated Bill for Ham Slice (per pack) = "<<tothammt << "\n"; break;
                     case 3: cout<<"  How Many Kilo/s of Pork Chop? = ";
                             cin>> mqty3;
                        totchopmt=totchopmt +(mqty3 * 450);
                        cout<<"Updated  Bill for Pork Chop (per kilo) = "<<totchopmt << "\n"; break;

                    }
               }
				while (mt<=3);
                break;
                }
                
        case 2:{
            do{
            cout<<"\n      Beef";
            cout<<"\n      1. Beef Chuck (per kilo) - P450.00 ";
            cout<<"\n      2. Ground Beef (per kilo) - P350.00 ";
            cout<<"\n      3. Strip Loin (per grams) - P400.00 ";
            cout<<"\n      4. Return";
              cout<<"\n    Choose your preferred[1-4]:";
              cin>>mt;
              if(mt>4){
                cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
                    switch(mt)
                    {case 1: cout<<"  How Many Kilo/s of Beef Chunk? = ";
                        cin>> mqty4;
                        totchuckmt= totchuckmt +(mqty4 * 450);
                        cout<<"Updated Bill for Beef Chuck (per kilo) = "<<totchuckmt << "\n"; break;
                    case 2: cout<<"  How Many Kilo/s of Ground Beef? = ";
                             cin>> mqty5;
                        totgroundmt= totgroundmt+(mqty5 * 350);
                        cout<<"Updated Bill for Beef Noodles = "<<totgroundmt << "\n"; break;
                     case 3: cout<<"  How Many Gram/s of Strip Loin? = ";
                             cin>> mqty6;
                        totstripmt=totstripmt +(mqty6 * 400);
                        cout<<"Updated Bill for Pork Noodles = "<<totstripmt << "\n"; break;

                    }
               }
                while (mt<=3);
                break;
                }
        case 3:{
            do{
            cout<<"\n      Chicken";
            cout<<"\n      1. Wings (pero kilo) - P190.00";
            cout<<"\n      2. Thighs (pero kilo) - P190.00";
            cout<<"\n      3. Breast (per kilo) - P190.00";
            cout<<"\n      4. Return";
              cout<<"\n    Choose your preferred[1-4]:";
              cin>>mt;
              if(mt>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
                    switch(mt)
                    {case 1: cout<<"  How Many Kilo/s of Wings? = ";
                        cin>> mqty7;
                        totwingmt= totwingmt + (mqty7 * 190);
                        cout<<"Updated Bill for Wings (per kilo) = "<<totwingmt << "\n"; break;
                    case 2: cout<<"  How Many Kilo/s of Thigh? = ";
                             cin>> mqty8;
                        totthighmt= totthighmt + (mqty8 * 190);
                        cout<<"Updated  Bill for Thigh (per kilo) = "<<totthighmt << "\n"; break;
                     case 3: cout<<"  How Many Kilo/s of Breast? = ";
                             cin>> mqty9;
                        totbreastmt=totbreastmt + (mqty9 * 190);
                        cout<<"Updated Bill for Breast (per kilo) = "<<totbreastmt << "\n"; break;

                    }
               }
                while (mt<=3);
                break;
                default: cout<<" ";
                }
                        }
        }while (mt<=3);
	}
        }
        switch(trans){
    case 3:{
    do {
    	do{
	cout<<"\n   1. Soju";
	cout<<"\n   2. Juices";
	cout<<"\n   3. Soda";
	cout<<"\n   Choose your preferred[1-3]:";
	cin>>ds;
	if(ds>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
		}while(ds>4);
	switch(ds){
		case 1:{ //3*
			do{
			cout<<"\n      Soju";
			cout<<"\n      1. Soju Lemon Flavored (360 ml) - P130.00";
			cout<<"\n      2. Soju Citrus Flavored (360 ml) - P130.00";
			cout<<"\n      3. Soju Blue Berry Flavored (360 ml) - P130.00";
			cout<<"\n      4. Return";
			cout<<"\n    Choose your preferred[1-4]:";
			cin>>ds;
			if(ds>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
			switch(ds)
				{case 1: cout<<"  How Many Bottle of Soju Lemon Flavored? = ";
				cin>>dqty1;
				totsjlemon= totsjlemon +(dqty1 * 130);
				cout<<"Updated Bill for Soju Lemon Flavored (per bottle) = "<<totsjlemon<< "\n"; break;
				case 2: cout<<"  How Many Bottle of Soju Citrus Flavored? = ";
				cin>>dqty2;
				totsjcitrus= totsjcitrus+(dqty2 * 130);
				cout<<"Updated Bill for Soju Lemon Flavored (per bottle) = "<<totsjcitrus<< "\n"; break;
                case 3: cout<<"  How Many Bottle of Soju Blue Berry Flavored? = ";
				cin>>dqty3;
				totsjbberry=totsjbberry +(dqty3 * 130);
				cout<<"Updated  Bill for Soju Blue Berry Flavored (per bottle) = "<<totsjbberry<< "\n"; break;}
            }while (ds<=3);
				break;}
        case 2:{
		do{
		cout<<"\n      Juices";
		cout<<"\n      1. Lemon Juice (1000 ml) - P25.00 ";
		cout<<"\n      2. Orange Juice (1000 ml) - P25.00 ";
		cout<<"\n      3. Apple Juice (1000 ml) - P25.00 ";
		cout<<"\n      4. Return";
		cout<<"\n    Choose your preferred[1-4]:";
		cin>>ds;
		if(ds>4){
              cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
			switch(ds)
				{case 1: cout<<"  How Many Bottle of Lemon Juice? = ";
				cin>>dqty4;
				totlemonj= totlemonj +(dqty4 * 25);
				cout<<"Updated Bill for Lemon Juice (per bottle) = "<<totlemonj<< "\n"; break;
				case 2: cout<<"  How Many Bottle of Orange Juice? = ";
				cin>>dqty5;
				totorangej= totorangej+(dqty5 * 25);
				cout<<"Updated Bill for Orange Juice (per bottle) = "<<totorangej<< "\n"; break;
				case 3: cout<<"  How Many Bottle of Apple Juice? = ";
				cin>>dqty6;
				totapplej=totapplej +(dqty6 * 25);
				cout<<"Updated Bill for Apple Juice (per bottle) = "<<totapplej<< "\n"; break;}
        	}while (ds<=3);
				break;}
        case 3:{
			do{
			cout<<"\n      Soda";
			cout<<"\n      1. Coke (250 ml) - P17.00";
			cout<<"\n      1. 7 UP (250 ml) - P 15.00";
			cout<<"\n      3. Pepsi (250 ml) - P15.00";
			cout<<"\n      4. Return";
			cout<<"\n    Choose your preferred[1-4]:";
			cin>>ds;
			if(ds>4){
              	cout<<"\n---------------------------------------------------------\n";
              	cout<<"            Please choose from numbers 1-4 only!";
              	cout<<"\n---------------------------------------------------------\n";
			  }
				switch(ds)
					{case 1: cout<<"  How Many Bottle of Coke? = ";
					cin>>dqty7;
					totcoke= totcoke +(dqty7 * 17);
					cout<<"Updated Bill for Coke (per bottle) = "<<totcoke<< "\n"; break;
                    case 2: cout<<"  How Many Bottle of 7 up? = ";
					cin>>dqty8;
					tot7up= tot7up +(dqty8 * 15);
					cout<<"Updated  Bill for 7 up (per bottle) = "<<tot7up<< "\n"; break;
					case 3: cout<<"  How Many Bottle of Pepsi? = ";
					cin>>dqty9;
					totpepsi=totpepsi +(dqty9 * 15);
					cout<<"Updated Bill for Pepsi (per bottle) = "<<totpepsi<< "\n"; break;}
               }while (ds<=3);
					break;
                		default: cout<<"";
                }
                        }
        }while (ds<=3);
    
		}
		
				break;
			
		}
        }while (trans<=3);
system("cls");
time_t now;

struct tm nowLocal;

now=time (NULL);

nowLocal=*localtime(&now);
cout<<"Date: "<<nowLocal.tm_mday<<"/"<<nowLocal.tm_mon+1<<"/"<<nowLocal.tm_year+1900<<"\n";
cout<<"Time: "<<nowLocal.tm_hour<<":"<<nowLocal.tm_min<<":"<<nowLocal.tm_sec<<"\n";
cin.get();
cout<<"Costumer Name: "<<name<<"\n";
cout<<"\n---------------------------------------------------------\n";
cout<<"                   Summary of Purchases\n";
cout<<"---------------------------------------------------------\n";
cout<<"        ORDER                  |   QUANTITY    |   TOTAL\n";
if(qty1>=1)
	cout<<" Hot and Spicy Noodles         |    "<<qty1<<"          "<<"| = "<<tothnsndl <<"\n";
if (qty2>=1)
	cout<<" Sweet and Spicy Noodles       |    "<<qty2<<"          "<<"| = "<<totsnsndl <<"\n";
	if (qty3>=1)
	cout<<" Triple Hot and Spicy Noodles  |    "<<qty3<<"          "<<"| = "<<totthnsndl <<"\n";
	if (qty4>=1)
	cout<<" Chicken Noodles               |    "<<qty4<<"          "<<"| = "<<totchindl <<"\n";
	if (qty5>=1)
	cout<<" Beef Noodles                  |    "<<qty5<<"          "<<"| = "<<totbeefndl <<"\n";
	if (qty6>=1)
	cout<<" Pork Noodles                  |    "<<qty6<<"          "<<"| = "<<totporkndl <<"\n";
	if (qty7>=1)
	cout<<" Hot Chicken Flavor Ramen      |    "<<qty7<<"          "<<"| = "<<tothcframen <<"\n";
	if (qty8>=1)
	cout<<" Spicy Barbecue Flavor Ramen   |    "<<qty8<<"          "<<"| = "<<totsbframen <<"\n";
	if (qty9>=1)
	cout<<" Cheese Flavor Ramen           |    "<<qty9<<"          "<<"| = "<<totsbframen <<"\n";
	if (mqty1>=1)
	cout<<" Bacon (per pack)              |    "<<mqty1<<"          "<<"| = "<<totbaconmt <<"\n";

	if (mqty2>=1)
	cout<<" Ham Slice (per pack)          |    "<<mqty2<<"          "<<"| = "<<tothammt   <<"\n";
	if (mqty3>=1)
	cout<<" Pork Chop (per kilo)          |    "<<mqty3<<"          "<<"| = "<<totchopmt  <<"\n";
	if (mqty4>=1)
	cout<<" Beef Chuck (per kilo)         |    "<<mqty4<<"          "<<"| = "<<totchuckmt  <<"\n";
	if (mqty5>=1)
	cout<<" Groud Beef (per kilo)         |    "<<mqty5<<"          "<<"| = "<<totgroundmt   <<"\n";
	if (mqty6>=1)
	cout<<" Strip Loin (per grams)        |    "<<mqty6<<"          "<<"| = "<<totstripmt <<"\n";
	if (mqty7>=1)
	cout<<" Wings (per kilo)              |    "<<mqty7<<"          "<<"| = "<<totwingmt  <<"\n";
	if (mqty8>=1)
	cout<<" Thigh (per kilo)              |    "<<mqty8<<"          "<<"| = "<<totthighmt <<"\n";
	if (mqty9>=1)
	cout<<" Breast (per kilo)             |    "<<mqty9<<"          "<<"| = "<<totbreastmt <<"\n";
	if (dqty1>=1)
	cout<<" Soju Lemon Flavored (360 ml)  |    "<<dqty1<<"          "<<"| = "<<totsjlemon<<"\n";
	if (dqty2>=1)
	cout<<" Soju Citrus Flavored (360 ml) |    "<<dqty2<<"          "<<"| = "<<totsjcitrus<<"\n";
	if (dqty3>=1)
	cout<<" Soju B.Berry Flavored (360 ml)|    "<<dqty3<<"          "<<"| = "<<totsjbberry<<"\n";
	if (dqty4>=1)
	cout<<" Lemon Juice (1000 ml)         |    "<<dqty4<<"          "<<"| = "<<totlemonj<<"\n";
	if (dqty5>=1)
	cout<<" Orange Juice (1000 ml)        |    "<<dqty5<<"          "<<"| = "<<totorangej<<"\n";
	if (dqty6>=1)
	cout<<" Apple Juice (1000 ml)         |    "<<dqty6<<"          "<<"| = "<<totapplej<<"\n";
	if (dqty7>=1)
	cout<<" Coke (250 ml)                 |    "<<dqty7<<"          "<<"| = "<<totcoke<<"\n";
	if (dqty8>=1)
	cout<<" 7 up (250 ml)                 |    "<<dqty8<<"          "<<"| = "<<tot7up<<"\n";
	if (dqty9>=1)
	cout<<" Pepsi (250 ml)                |    "<<dqty9<<"          "<<"| = "<<totpepsi<<"\n";
totbill = tothnsndl+totsnsndl+totthnsndl+totbill+change+totchindl+totbeefndl+totporkndl+tothcframen+totsbframen+totcframen+totbaconmt+tothammt+totchopmt+totchuckmt+totgroundmt+totstripmt+totwingmt+totthighmt+totbreastmt+totsjlemon+totsjcitrus+totsjbberry+totlemonj+totorangej+totapplej+totcoke+tot7up+totpepsi;
cout<<" Total Orders Bill       = "<<totbill <<"\n";
cout<<"---------------------------------------------------------\n";


do{
cout<<"  Enter Payment          = ";
cin>>pay;
change = pay - totbill;
if (pay<totbill){
	cout<<"---------------------------------------------------------\n";
	cout<<"                   Insufficient funds";
	cout<<"\n   We're sorry but we cannot process the transaction.\n";
	cout<<"---------------------------------------------------------\n";
}
}while (pay<totbill);
cout<<"  Your Change            = "<<change;
cout<<"\n---------------------------------------------------------\n";
cout<<"\n	     Thank you!! Please come again!!!			 \n";
}