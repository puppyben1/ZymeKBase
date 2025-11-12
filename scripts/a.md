|      |                                                              |
| ---- | ------------------------------------------------------------ |
|      |                                                              |
|      | <!DOCTYPE html>                                              |
|      | <html lang="en">                                             |
|      |                                                              |
|      | <head>                                                       |
|      | <link rel="shortcut icon" href="[/static/img/LOGO/icon-03.png](https://dizyme.aicidlab.itmo.ru/static/img/LOGO/icon-03.png)" type="image/x-icon" /> |
|      | <meta charset="UTF-8">                                       |
|      | <meta http-equiv="X-UA-Compatible" content="IE=edge">        |
|      | <meta name="viewport" content="width=device-width, initial-scale=1.0"> |
|      | <title>                                                      |
|      | DiZyme \| Database                                           |
|      |                                                              |
|      | </title>                                                     |
|      |                                                              |
|      | <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"> |
|      | <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"> |
|      | <link rel="stylesheet" href="https://cdn.datatables.net/1.13.5/css/jquery.dataTables.min.css"> |
|      |                                                              |
|      | <link rel="stylesheet" type="text/css" href="[/static/style.css ](https://dizyme.aicidlab.itmo.ru/static/style.css)"> |
|      | </head>                                                      |
|      |                                                              |
|      | <body>                                                       |
|      | <!--  HEADER  -->                                            |
|      | <header class="header">                                      |
|      |                                                              |
|      | <a href="[/](https://dizyme.aicidlab.itmo.ru/)" class="logo"> |
|      | <img src="[/static/img/LOGO/logo_fin-02.png](https://dizyme.aicidlab.itmo.ru/static/img/LOGO/logo_fin-02.png)" alt=""> |
|      | </a>                                                         |
|      | <!--  NAVBAR  -->                                            |
|      | <nav class="navbar">                                         |
|      | <div class="dropdown">                                       |
|      | <a href="[/apps/](https://dizyme.aicidlab.itmo.ru/apps/)">PREDICTION</a> |
|      | <div class="dropdown-content">                               |
|      | <a href="[/apps/multi](https://dizyme.aicidlab.itmo.ru/apps/multi)">EXPLORATIVE</a> |
|      | <a href="[/apps/multi1](https://dizyme.aicidlab.itmo.ru/apps/multi1)">DETAILED</a> |
|      | <a href="[/apps/multipro](https://dizyme.aicidlab.itmo.ru/apps/multipro)">CUSTOMISED</a> |
|      | </div>                                                       |
|      | </div>                                                       |
|      | <a href="[/assistant-bot/](https://dizyme.aicidlab.itmo.ru/assistant-bot/)">ASSISTANT</a> |
|      | <a href="[/database/](https://dizyme.aicidlab.itmo.ru/database/)">DATABASE</a> |
|      | <a href="[/database/vis](https://dizyme.aicidlab.itmo.ru/database/vis)">VISUALISATION</a> |
|      | <a href="[/database/add](https://dizyme.aicidlab.itmo.ru/database/add)">OFFER A SAMPLE</a> |
|      | <a href="[/info](https://dizyme.aicidlab.itmo.ru/info)">INFORMATION</a> |
|      | <div class="login-signup">                                   |
|      | <a href="[#](https://dizyme.aicidlab.itmo.ru/database/#)">Login</a> <a href="[#contact](https://dizyme.aicidlab.itmo.ru/database/#contact)">Signup</a> |
|      | </div>                                                       |
|      |                                                              |
|      | </nav>                                                       |
|      | </div>                                                       |
|      |                                                              |
|      | <div class="header-right">                                   |
|      | <div class="login-signup">                                   |
|      | <a href="[/users/login/](https://dizyme.aicidlab.itmo.ru/users/login/)">Login</a> <a href="[#contact](https://dizyme.aicidlab.itmo.ru/database/#contact)">Signup</a> |
|      | </div>                                                       |
|      |                                                              |
|      | <div class="icons">                                          |
|      | <div class="fas fa-bars" id="menu-btn"></div>                |
|      | </div>                                                       |
|      | </div>                                                       |
|      |                                                              |
|      | </header>                                                    |
|      |                                                              |
|      | <section class="container_full">                             |
|      | <div class="container">                                      |
|      | <div class="col-md-12">                                      |
|      | <h2>Nanozymes database</h2>                                  |
|      | </div>                                                       |
|      | <br>                                                         |
|      |                                                              |
|      | </div>                                                       |
|      | <table id="example" class="table table-striped" style="width: 70%"> |
|      | <thead>                                                      |
|      | <tr>                                                         |
|      | <th>Chemical formula</th>                                    |
|      | <th>Catalytic activity</th>                                  |
|      | <th>Michaelis–Menten constant (Km), mM</th>                  |
|      | <th>Maximum reaction velocity (Vmax), mM/s</th>              |
|      | <th>Link to article</th>                                     |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      | </thead>                                                     |
|      | <tbody>                                                      |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0065</td>                                              |
|      | <td>1.3763</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0554</td>                                              |
|      | <td>0.2643</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0355</td>                                              |
|      | <td>8.363</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2277</td>                                              |
|      | <td>0.4382</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0173</td>                                              |
|      | <td>1.0272</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0243</td>                                              |
|      | <td>0.6753</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0348</td>                                              |
|      | <td>0.6468</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0393</td>                                              |
|      | <td>1.2813</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0661</td>                                              |
|      | <td>0.9203</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1107</td>                                              |
|      | <td>1.0422</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C4RA15675G">https://doi.org/10.1039/C4RA15675G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0752</td>                                              |
|      | <td>0.000255451</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C1CC14300J">https://doi.org/10.1039/C1CC14300J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0015</td>                                              |
|      | <td>6.98</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0964</td>                                              |
|      | <td>0.353</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0258</td>                                              |
|      | <td>1.55</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.033</td>                                               |
|      | <td>0.73</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.112</td>                                               |
|      | <td>7.15</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.543</td>                                               |
|      | <td>0.515</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.242</td>                                               |
|      | <td>4.94</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.304</td>                                               |
|      | <td>1.76</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5DT01585E">https://doi.org/10.1039/C5DT01585E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.605</td>                                               |
|      | <td>0.0000538</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2011.08.008">https://doi.org/10.1016/j.colsurfa.2011.08.008</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.528</td>                                               |
|      | <td>0.0000215</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2011.08.008">https://doi.org/10.1016/j.colsurfa.2011.08.008</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MgFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.67</td>                                                |
|      | <td>0.0000209</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.048">https://doi.org/10.1016/j.bios.2014.07.048</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MgFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.0001254</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.048">https://doi.org/10.1016/j.bios.2014.07.048</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MgFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>4.61</td>                                                |
|      | <td>0.0001346</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.048">https://doi.org/10.1016/j.bios.2014.07.048</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.55</td>                                                |
|      | <td>0.0000457</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.048">https://doi.org/10.1016/j.bios.2014.07.048</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.46</td>                                                |
|      | <td>0.0001748</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.048">https://doi.org/10.1016/j.bios.2014.07.048</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>2.6</td>                                                 |
|      | <td>0.0001411</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.048">https://doi.org/10.1016/j.bios.2014.07.048</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>490.72</td>                                              |
|      | <td>0.0000632</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5NJ02547H">https://doi.org/10.1039/C5NJ02547H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.509</td>                                               |
|      | <td>0.0000918</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5NJ02547H">https://doi.org/10.1039/C5NJ02547H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.85</td>                                                |
|      | <td>0.0001331</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac300939z">https://doi.org/10.1021/ac300939z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>1.66</td>                                                |
|      | <td>0.0000774</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac300939z">https://doi.org/10.1021/ac300939z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.142</td>                                               |
|      | <td>0.00002223</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.aca.2016.11.035">https://doi.org/10.1016/j.aca.2016.11.035</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>9.406</td>                                               |
|      | <td>0.0002584</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.aca.2016.11.035">https://doi.org/10.1016/j.aca.2016.11.035</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CdCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.317</td>                                               |
|      | <td>0.0000219</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04298-4">https://doi.org/10.1007/s00604-020-04298-4</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CdCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.325</td>                                               |
|      | <td>0.0000375</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04298-4">https://doi.org/10.1007/s00604-020-04298-4</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuWO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2</td>                                                 |
|      | <td>0.00472</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.06.175">https://doi.org/10.1016/j.snb.2017.06.175</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuWO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.38</td>                                                |
|      | <td>0.000113</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.06.175">https://doi.org/10.1016/j.snb.2017.06.175</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeWO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.18</td>                                                |
|      | <td>0.0001148</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ie504114v">https://doi.org/10.1021/ie504114v</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeWO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.59</td>                                                |
|      | <td>0.0000218</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ie504114v">https://doi.org/10.1021/ie504114v</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co2V2O7</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.311</td>                                               |
|      | <td>0.0000258</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsabm.9b01107">https://doi.org/10.1021/acsabm.9b01107</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co2V2O7</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.669</td>                                               |
|      | <td>0.0000125</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsabm.9b01107">https://doi.org/10.1021/acsabm.9b01107</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeVO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.691</td>                                               |
|      | <td>0.0000251</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.04.041">https://doi.org/10.1016/j.snb.2016.04.041</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeVO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0732</td>                                              |
|      | <td>0.0000272</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.04.041">https://doi.org/10.1016/j.snb.2016.04.041</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgVO3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.333</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2562-z">https://doi.org/10.1007/s00604-017-2562-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgVO3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.3</td>                                                 |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2562-z">https://doi.org/10.1007/s00604-017-2562-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgVO3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0412</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/jccs.201700031">https://doi.org/10.1002/jccs.201700031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgVO3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>5.291</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/jccs.201700031">https://doi.org/10.1002/jccs.201700031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMoO4</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.077</td>                                               |
|      | <td>0.0005105</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04376-7">https://doi.org/10.1007/s00604-020-04376-7</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgVO3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>8.03</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1670-x">https://doi.org/10.1007/s00604-015-1670-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgVO3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>14</td>                                                  |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1670-x">https://doi.org/10.1007/s00604-015-1670-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMoO4</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>1.115</td>                                               |
|      | <td>0.0001162</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04376-7">https://doi.org/10.1007/s00604-020-04376-7</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuMnO2</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.577</td>                                               |
|      | <td>0.0000815</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.09.120">https://doi.org/10.1016/j.snb.2018.09.120</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuMnO2</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>27.653</td>                                              |
|      | <td>0.0002765</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.09.120">https://doi.org/10.1016/j.snb.2018.09.120</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu0.89Zn0.11O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>10</td>                                                  |
|      | <td>0.00002877</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.6b05354">https://doi.org/10.1021/acsami.6b05354</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu0.89Zn0.11O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>71</td>                                                  |
|      | <td>0.000003</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.6b05354">https://doi.org/10.1021/acsami.6b05354</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2(MoO4)3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>1.126</td>                                               |
|      | <td>0.0000373</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-016-1955-8">https://doi.org/10.1007/s00604-016-1955-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2(MoO4)3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.106</td>                                               |
|      | <td>0.0000751</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-016-1955-8">https://doi.org/10.1007/s00604-016-1955-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(CeO2)0.10/CoO</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.245</td>                                               |
|      | <td>0.0001478</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.0c06920">https://doi.org/10.1021/acssuschemeng.0c06920</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(CeO2)0.10/CoO</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.133</td>                                               |
|      | <td>0.001101</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.0c06920">https://doi.org/10.1021/acssuschemeng.0c06920</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoO/CeO2</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>1.81</td>                                                |
|      | <td>0.000027</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apmt.2019.03.009">https://doi.org/10.1016/j.apmt.2019.03.009</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoO/CeO2</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.021</td>                                               |
|      | <td>0.000028</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apmt.2019.03.009">https://doi.org/10.1016/j.apmt.2019.03.009</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/CeO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.36</td>                                                |
|      | <td>0.0001666</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/CeO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>132.21</td>                                              |
|      | <td>0.0000434</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4@CeO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.15</td>                                                |
|      | <td>0.0000064</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2017.12.011">https://doi.org/10.1016/j.jtice.2017.12.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4@CeO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>1.13</td>                                                |
|      | <td>0.000125</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2017.12.011">https://doi.org/10.1016/j.jtice.2017.12.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd/CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.39</td>                                                |
|      | <td>0.0000594</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-018-2657-x">https://doi.org/10.1007/s10853-018-2657-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd/CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>9.43</td>                                                |
|      | <td>0.0000191</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-018-2657-x">https://doi.org/10.1007/s10853-018-2657-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce-Fe3O4</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.018</td>                                               |
|      | <td>0.0000125</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7AY00750G">https://doi.org/10.1039/C7AY00750G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce-Fe3O4</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>6.942</td>                                               |
|      | <td>0.0005</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C7AY00750G">https://doi.org/10.1039/C7AY00750G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-MnO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.101</td>                                               |
|      | <td>0.0000057</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.procbio.2019.05.014">https://doi.org/10.1016/j.procbio.2019.05.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-MnO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.041</td>                                               |
|      | <td>0.0000294</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.procbio.2019.05.014">https://doi.org/10.1016/j.procbio.2019.05.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt-WO2.72</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.105</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00216-019-02268-1">https://doi.org/10.1007/s00216-019-02268-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt-WO2.72</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>8.45</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00216-019-02268-1">https://doi.org/10.1007/s00216-019-02268-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.107</td>                                               |
|      | <td>0.0000362</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7AY00750G">https://doi.org/10.1039/C7AY00750G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>155</td>                                                 |
|      | <td>0.0000911</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7AY00750G">https://doi.org/10.1039/C7AY00750G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.23</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/chem.201001789">https://doi.org/10.1002/chem.201001789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.46</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/chem.201001789">https://doi.org/10.1002/chem.201001789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.58</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/chem.201001789">https://doi.org/10.1002/chem.201001789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.89</td>                                                |
|      | <td>0.0001493</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.procbio.2019.05.014">https://doi.org/10.1016/j.procbio.2019.05.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>2.46</td>                                                |
|      | <td>0.0000962</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.procbio.2019.05.014">https://doi.org/10.1016/j.procbio.2019.05.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.41</td>                                                |
|      | <td>0.0000396</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.procbio.2019.05.014">https://doi.org/10.1016/j.procbio.2019.05.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.34</td>                                                |
|      | <td>0.0000775</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.procbio.2019.05.014">https://doi.org/10.1016/j.procbio.2019.05.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>25</td>                                                  |
|      | <td>0.0001049</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.6b05354">https://doi.org/10.1021/acsami.6b05354</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>400</td>                                                 |
|      | <td>0.000161</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.6b05354">https://doi.org/10.1021/acsami.6b05354</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>GeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.42</td>                                                |
|      | <td>0.00023397</td>                                          |
|      | <td><a href="https://doi.org/10.1002/adfm.202001933">https://doi.org/10.1002/adfm.202001933</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>GeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.75</td>                                                |
|      | <td>0.000234</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adfm.202001933">https://doi.org/10.1002/adfm.202001933</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.014</td>                                               |
|      | <td>0.0000041</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.saa.2019.117412">https://doi.org/10.1016/j.saa.2019.117412</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>8.85</td>                                                |
|      | <td>0.000052</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.saa.2019.117412">https://doi.org/10.1016/j.saa.2019.117412</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WO3</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>10.6</td>                                                |
|      | <td>0.0000153</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2019.06.003">https://doi.org/10.1016/j.talanta.2019.06.003</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WO3</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1260</td>                                                |
|      | <td>0.00003</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2019.06.003">https://doi.org/10.1016/j.talanta.2019.06.003</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WO2.92</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.79</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.aca.2017.09.011">https://doi.org/10.1016/j.aca.2017.09.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WO2.92</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>1.26</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.aca.2017.09.011">https://doi.org/10.1016/j.aca.2017.09.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>W18O49</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.003</td>                                               |
|      | <td>0.00124</td>                                             |
|      | <td><a href="https://doi.org/10.1007/s11051-018-4271-x">https://doi.org/10.1007/s11051-018-4271-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>W18O49</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>8.734</td>                                               |
|      | <td>0.00122</td>                                             |
|      | <td><a href="https://doi.org/10.1007/s11051-018-4271-x">https://doi.org/10.1007/s11051-018-4271-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2</td>                                                 |
|      | <td>0.0000559</td>                                           |
|      | <td><a href="https://doi.org/10.1166/jnn.2018.13977">https://doi.org/10.1166/jnn.2018.13977</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>572.98</td>                                              |
|      | <td>0.0000977</td>                                           |
|      | <td><a href="https://doi.org/10.1166/jnn.2018.13977">https://doi.org/10.1166/jnn.2018.13977</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>92.3</td>                                                |
|      | <td>0.0000311</td>                                           |
|      | <td><a href="https://doi.org/10.1166/jnn.2018.13977">https://doi.org/10.1166/jnn.2018.13977</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>546.6</td>                                               |
|      | <td>0.0000504</td>                                           |
|      | <td><a href="https://doi.org/10.1166/jnn.2018.13977">https://doi.org/10.1166/jnn.2018.13977</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.298</td>                                               |
|      | <td>0.0000736</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8TB01132J">https://doi.org/10.1039/C8TB01132J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>146.7</td>                                               |
|      | <td>0.0000637</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8TB01132J">https://doi.org/10.1039/C8TB01132J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0997</td>                                              |
|      | <td>0.00052</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C9TB00989B">https://doi.org/10.1039/C9TB00989B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>144.3</td>                                               |
|      | <td>0.0000184</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9TB00989B">https://doi.org/10.1039/C9TB00989B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.5304</td>                                              |
|      | <td>0.0000543</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9TB00989B">https://doi.org/10.1039/C9TB00989B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>127.92</td>                                              |
|      | <td>0.0000377</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9TB00989B">https://doi.org/10.1039/C9TB00989B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.768</td>                                               |
|      | <td>0.000005</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C1CY00124H">https://doi.org/10.1039/C1CY00124H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.957</td>                                               |
|      | <td>0.0000063</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C1CY00124H">https://doi.org/10.1039/C1CY00124H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.257</td>                                               |
|      | <td>0.0000165</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C1CY00124H">https://doi.org/10.1039/C1CY00124H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.317</td>                                               |
|      | <td>0.0000153</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C1CY00124H">https://doi.org/10.1039/C1CY00124H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.518</td>                                               |
|      | <td>0.0000106</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C1CY00124H">https://doi.org/10.1039/C1CY00124H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.098</td>                                               |
|      | <td>0.0000344</td>                                           |
|      | <td><a href="https://doi.org/10.1038/nnano.2007.260">https://doi.org/10.1038/nnano.2007.260</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>154</td>                                                 |
|      | <td>0.0000978</td>                                           |
|      | <td><a href="https://doi.org/10.1038/nnano.2007.260">https://doi.org/10.1038/nnano.2007.260</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.374</td>                                               |
|      | <td>0.000026</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.colsurfb.2017.02.004">https://doi.org/10.1016/j.colsurfb.2017.02.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>54.6</td>                                                |
|      | <td>0.000018</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.colsurfb.2017.02.004">https://doi.org/10.1016/j.colsurfb.2017.02.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.26</td>                                                |
|      | <td>0.00000351</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.9b04116">https://doi.org/10.1021/acs.analchem.9b04116</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>6.66</td>                                                |
|      | <td>0.00000129</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.9b04116">https://doi.org/10.1021/acs.analchem.9b04116</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.295</td>                                               |
|      | <td>0.0000072</td>                                           |
|      | <td><a href="https://doi.org/10.1021/jacs.7b00601">https://doi.org/10.1021/jacs.7b00601</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.27</td>                                                |
|      | <td>0.000035</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jacs.7b00601">https://doi.org/10.1021/jacs.7b00601</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.233</td>                                               |
|      | <td>0.000176</td>                                            |
|      | <td><a href="https://doi.org/10.1021/am405009f">https://doi.org/10.1021/am405009f</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>479.91</td>                                              |
|      | <td>0.000275</td>                                            |
|      | <td><a href="https://doi.org/10.1021/am405009f">https://doi.org/10.1021/am405009f</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.103</td>                                               |
|      | <td>0.000256</td>                                            |
|      | <td><a href="https://doi.org/10.1021/am405009f">https://doi.org/10.1021/am405009f</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>173.51</td>                                              |
|      | <td>0.000189</td>                                            |
|      | <td><a href="https://doi.org/10.1021/am405009f">https://doi.org/10.1021/am405009f</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.018</td>                                               |
|      | <td>0.000024</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C4TB00968A">https://doi.org/10.1039/C4TB00968A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.77</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C4TB00968A">https://doi.org/10.1039/C4TB00968A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/CeO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.36</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/CeO2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>132.21</td>                                              |
|      | <td>0.0000434</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.51</td>                                                |
|      | <td>0.0001241</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>140.56</td>                                              |
|      | <td>0.0000343</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.42</td>                                                |
|      | <td>0.0001374</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>138.31</td>                                              |
|      | <td>0.0000398</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.01.068">https://doi.org/10.1016/j.snb.2019.01.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.063</td>                                               |
|      | <td>0.000019</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6NR00860G">https://doi.org/10.1039/C6NR00860G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.61</td>                                                |
|      | <td>0.000032</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6NR00860G">https://doi.org/10.1039/C6NR00860G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.079</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2016.12.067">https://doi.org/10.1016/j.apsusc.2016.12.067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.015</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2016.12.067">https://doi.org/10.1016/j.apsusc.2016.12.067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.091</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2016.12.067">https://doi.org/10.1016/j.apsusc.2016.12.067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.013</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2016.12.067">https://doi.org/10.1016/j.apsusc.2016.12.067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0262</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2016.12.067">https://doi.org/10.1016/j.apsusc.2016.12.067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.012</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2016.12.067">https://doi.org/10.1016/j.apsusc.2016.12.067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.037</td>                                               |
|      | <td>0.0000627</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C2CC17013B">https://doi.org/10.1039/C2CC17013B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>140.07</td>                                              |
|      | <td>0.000121</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C2CC17013B">https://doi.org/10.1039/C2CC17013B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0151</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/ie403554v">https://doi.org/10.1021/ie403554v</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.8268</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/ie403554v">https://doi.org/10.1021/ie403554v</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.082</td>                                               |
|      | <td>0.0000655</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8NR06162A">https://doi.org/10.1039/C8NR06162A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>2.22</td>                                                |
|      | <td>0.0001182</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8NR06162A">https://doi.org/10.1039/C8NR06162A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.283</td>                                               |
|      | <td>0.0001052</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2020.112342">https://doi.org/10.1016/j.bios.2020.112342</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>5.9322</td>                                              |
|      | <td>0.0000985</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2020.112342">https://doi.org/10.1016/j.bios.2020.112342</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.000000332</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C1JM14253D">https://doi.org/10.1039/C1JM14253D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>245</td>                                                 |
|      | <td>0.000285</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C1JM14253D">https://doi.org/10.1039/C1JM14253D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3</td>                                                 |
|      | <td>0.0000843</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9NJ05955E">https://doi.org/10.1039/C9NJ05955E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>2.97</td>                                                |
|      | <td>0.0000767</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9NJ05955E">https://doi.org/10.1039/C9NJ05955E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.000035</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C9NJ05955E">https://doi.org/10.1039/C9NJ05955E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.62</td>                                                |
|      | <td>0.0000313</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9NJ05955E">https://doi.org/10.1039/C9NJ05955E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.24</td>                                                |
|      | <td>0.000004</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep35344">https://doi.org/10.1038/srep35344</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.217</td>                                               |
|      | <td>0.000082</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep35344">https://doi.org/10.1038/srep35344</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>153.6</td>                                               |
|      | <td>0.000122</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep35344">https://doi.org/10.1038/srep35344</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.046</td>                                               |
|      | <td>0.0000094</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C2AY25511A">https://doi.org/10.1039/C2AY25511A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>64.6</td>                                                |
|      | <td>0.0000507</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C2AY25511A">https://doi.org/10.1039/C2AY25511A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.269</td>                                               |
|      | <td>0.00001135</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.08.094">https://doi.org/10.1016/j.snb.2016.08.094</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>3.182</td>                                               |
|      | <td>0.00000926</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.08.094">https://doi.org/10.1016/j.snb.2016.08.094</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.274</td>                                               |
|      | <td>0.0000159</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.09.049">https://doi.org/10.1016/j.snb.2016.09.049</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.278</td>                                               |
|      | <td>0.0000087</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.09.049">https://doi.org/10.1016/j.snb.2016.09.049</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0753</td>                                              |
|      | <td>0.000000401</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.msec.2015.10.046">https://doi.org/10.1016/j.msec.2015.10.046</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.958</td>                                               |
|      | <td>0.00000259</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.msec.2015.10.046">https://doi.org/10.1016/j.msec.2015.10.046</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.67</td>                                                |
|      | <td>0.0000038</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2017.12.011">https://doi.org/10.1016/j.jtice.2017.12.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>2.5</td>                                                 |
|      | <td>0.0001667</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2017.12.011">https://doi.org/10.1016/j.jtice.2017.12.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.33</td>                                                |
|      | <td>0.0000026</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2017.12.011">https://doi.org/10.1016/j.jtice.2017.12.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.75</td>                                                |
|      | <td>0.0000833</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2017.12.011">https://doi.org/10.1016/j.jtice.2017.12.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.87</td>                                                |
|      | <td>0.00000259</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C8NJ00097B">https://doi.org/10.1039/C8NJ00097B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>12.45</td>                                               |
|      | <td>0.00000259</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C8NJ00097B">https://doi.org/10.1039/C8NJ00097B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.147</td>                                               |
|      | <td>0.00000259</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2015.04.039">https://doi.org/10.1016/j.biomaterials.2015.04.039</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>293</td>                                                 |
|      | <td>0.00000259</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2015.04.039">https://doi.org/10.1016/j.biomaterials.2015.04.039</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.016</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C2AN35072F">https://doi.org/10.1039/C2AN35072F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>41</td>                                                  |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C2AN35072F">https://doi.org/10.1039/C2AN35072F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.0000145</td>                                           |
|      | <td><a href="https://doi.org/10.1002/cjoc.201300683">https://doi.org/10.1002/cjoc.201300683</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.013</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/cctc.201100064">https://doi.org/10.1002/cctc.201100064</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>85.6</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/cctc.201100064">https://doi.org/10.1002/cctc.201100064</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.08</td>                                                |
|      | <td>0.0006</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.06.096">https://doi.org/10.1016/j.snb.2017.06.096</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.06</td>                                                |
|      | <td>0.0006</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.06.096">https://doi.org/10.1016/j.snb.2017.06.096</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.08</td>                                                |
|      | <td>0.00035</td>                                             |
|      | <td><a href="https://doi.org/10.1002/adfm.201800018">https://doi.org/10.1002/adfm.201800018</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.09</td>                                                |
|      | <td>0.00034</td>                                             |
|      | <td><a href="https://doi.org/10.1002/adfm.201800018">https://doi.org/10.1002/adfm.201800018</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.74</td>                                                |
|      | <td>0.0000442</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-018-2657-x">https://doi.org/10.1007/s10853-018-2657-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.45</td>                                                |
|      | <td>0.0000154</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-018-2657-x">https://doi.org/10.1007/s10853-018-2657-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>4.5</td>                                                 |
|      | <td>0.0000084</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-018-2657-x">https://doi.org/10.1007/s10853-018-2657-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>28.63</td>                                               |
|      | <td>0.000005</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s10853-018-2657-x">https://doi.org/10.1007/s10853-018-2657-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0004</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/adfm.201001302">https://doi.org/10.1002/adfm.201001302</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0029</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/adfm.201001302">https://doi.org/10.1002/adfm.201001302</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0843</td>                                              |
|      | <td>0.002809</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.microc.2019.104352">https://doi.org/10.1016/j.microc.2019.104352</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.238</td>                                               |
|      | <td>0.00273</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.microc.2019.104352">https://doi.org/10.1016/j.microc.2019.104352</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.165</td>                                               |
|      | <td>0.000024</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5RA11014A">https://doi.org/10.1039/C5RA11014A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.058</td>                                               |
|      | <td>0.000014</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5RA11014A">https://doi.org/10.1039/C5RA11014A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.146</td>                                               |
|      | <td>0.00000131</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C3TA15051H">https://doi.org/10.1039/C3TA15051H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.69</td>                                                |
|      | <td>0.00000177</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C3TA15051H">https://doi.org/10.1039/C3TA15051H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>UO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>6.423</td>                                               |
|      | <td>0.00000584</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-019-3624-1">https://doi.org/10.1007/s00604-019-3624-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>UO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.549</td>                                               |
|      | <td>0.00000629</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-019-3624-1">https://doi.org/10.1007/s00604-019-3624-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.0001256</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0RA05342B">https://doi.org/10.1039/D0RA05342B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>3.27</td>                                                |
|      | <td>0.0002257</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0RA05342B">https://doi.org/10.1039/D0RA05342B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.22</td>                                                |
|      | <td>0.00439</td>                                             |
|      | <td><a href="https://doi.org/10.3390/nano10020313">https://doi.org/10.3390/nano10020313</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2O</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.256</td>                                               |
|      | <td>0.00000758</td>                                          |
|      | <td><a href="https://doi.org/10.1039/D0TB03005H">https://doi.org/10.1039/D0TB03005H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2O</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.86</td>                                                |
|      | <td>0.0000181</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB03005H">https://doi.org/10.1039/D0TB03005H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2O</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.128</td>                                               |
|      | <td>0.0000111</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB03005H">https://doi.org/10.1039/D0TB03005H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2O</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.729</td>                                               |
|      | <td>0.0000268</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB03005H">https://doi.org/10.1039/D0TB03005H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2O</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.9</td>                                                 |
|      | <td>0.0001017</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121990">https://doi.org/10.1016/j.talanta.2020.121990</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2O</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>20.38</td>                                               |
|      | <td>0.0000838</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121990">https://doi.org/10.1016/j.talanta.2020.121990</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Cu2O</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.21</td>                                                |
|      | <td>0.0000608</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121990">https://doi.org/10.1016/j.talanta.2020.121990</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Cu2O</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>10.56</td>                                               |
|      | <td>0.0000668</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121990">https://doi.org/10.1016/j.talanta.2020.121990</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.099</td>                                               |
|      | <td>0.00021</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.0c07886">https://doi.org/10.1021/acsami.0c07886</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.146</td>                                               |
|      | <td>0.00021</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.0c07886">https://doi.org/10.1021/acsami.0c07886</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.29</td>                                                |
|      | <td>0.000039</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2017.11.064">https://doi.org/10.1016/j.jcis.2017.11.064</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>44.69</td>                                               |
|      | <td>0.0000223</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2017.11.064">https://doi.org/10.1016/j.jcis.2017.11.064</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.23</td>                                                |
|      | <td>0.0000475</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121680">https://doi.org/10.1016/j.talanta.2020.121680</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.4</td>                                                 |
|      | <td>0.000059</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121680">https://doi.org/10.1016/j.talanta.2020.121680</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaCoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.24</td>                                                |
|      | <td>0.000349</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7NJ01177F">https://doi.org/10.1039/C7NJ01177F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaCoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>15</td>                                                  |
|      | <td>0.00035</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C7NJ01177F">https://doi.org/10.1039/C7NJ01177F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaNiO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.105</td>                                               |
|      | <td>0.000362</td>                                            |
|      | <td><a href="https://doi.org/10.7150/thno.19257">https://doi.org/10.7150/thno.19257</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaNiO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>90.05</td>                                               |
|      | <td>0.0026</td>                                              |
|      | <td><a href="https://doi.org/10.7150/thno.19257">https://doi.org/10.7150/thno.19257</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeVO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.326</td>                                               |
|      | <td>0.0000361</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6TB01881E">https://doi.org/10.1039/C6TB01881E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeVO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.157</td>                                               |
|      | <td>0.0000853</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6TB01881E">https://doi.org/10.1039/C6TB01881E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Tb2(MoO4)3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.911</td>                                               |
|      | <td>0.0000101</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.saa.2017.06.006">https://doi.org/10.1016/j.saa.2017.06.006</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Tb2(MoO4)3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.035</td>                                               |
|      | <td>0.0000268</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.saa.2017.06.006">https://doi.org/10.1016/j.saa.2017.06.006</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni0.84Pd</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.11</td>                                                |
|      | <td>0.0000152</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6CC00194G">https://doi.org/10.1039/C6CC00194G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni0.84Pd</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.66</td>                                                |
|      | <td>0.0002618</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6CC00194G">https://doi.org/10.1039/C6CC00194G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiTe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.011</td>                                               |
|      | <td>0.0000427</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C4CC06684G">https://doi.org/10.1039/C4CC06684G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiTe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.361</td>                                               |
|      | <td>0.003097</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adhm.201500173">https://doi.org/10.1002/adhm.201500173</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.42</td>                                                |
|      | <td>0.0000302</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.aca.2014.10.011">https://doi.org/10.1016/j.aca.2014.10.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>84.07</td>                                               |
|      | <td>0.000037326</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.aca.2014.10.011">https://doi.org/10.1016/j.aca.2014.10.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.096</td>                                               |
|      | <td>0.0001414</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b01616">https://doi.org/10.1021/acsami.7b01616</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>3.07</td>                                                |
|      | <td>0.0001817</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b01616">https://doi.org/10.1021/acsami.7b01616</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.234</td>                                               |
|      | <td>0.0000825</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7RA10370K">https://doi.org/10.1039/C7RA10370K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>2.206</td>                                               |
|      | <td>0.000582667</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C7RA10370K">https://doi.org/10.1039/C7RA10370K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.155</td>                                               |
|      | <td>0.0000832</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>191</td>                                                 |
|      | <td>0.0000638</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.197</td>                                               |
|      | <td>0.000147</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>175</td>                                                 |
|      | <td>0.0000876</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.134</td>                                               |
|      | <td>0.0000965</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>213</td>                                                 |
|      | <td>0.000106</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.168</td>                                               |
|      | <td>0.000131</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>196</td>                                                 |
|      | <td>0.0000983</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s13205-017-1082-1">https://doi.org/10.1007/s13205-017-1082-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.062</td>                                               |
|      | <td>0.00055</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C6NR02730J">https://doi.org/10.1039/C6NR02730J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.000063</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6NR02730J">https://doi.org/10.1039/C6NR02730J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.06</td>                                                |
|      | <td>0.000269</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.msec.2015.10.046">https://doi.org/10.1016/j.msec.2015.10.046</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>36.6</td>                                                |
|      | <td>0.00000496</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.msec.2015.10.046">https://doi.org/10.1016/j.msec.2015.10.046</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0854</td>                                              |
|      | <td>0.00435</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.09.049">https://doi.org/10.1016/j.snb.2016.09.049</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.254</td>                                               |
|      | <td>0.0000131</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.09.049">https://doi.org/10.1016/j.snb.2016.09.049</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.088</td>                                               |
|      | <td>0.00000406</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.9b04116">https://doi.org/10.1021/acs.analchem.9b04116</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>30.24</td>                                               |
|      | <td>0.00000342</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.9b04116">https://doi.org/10.1021/acs.analchem.9b04116</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.24</td>                                                |
|      | <td>0.00017</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3</td>                                                 |
|      | <td>0.000125</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.22</td>                                                |
|      | <td>0.00024</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.55</td>                                                |
|      | <td>0.000096</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.69</td>                                                |
|      | <td>0.000046</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.71</td>                                                |
|      | <td>0.000042</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.73</td>                                                |
|      | <td>0.000145</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.81</td>                                                |
|      | <td>0.000115</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.96</td>                                                |
|      | <td>0.000052</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2</td>                                                 |
|      | <td>0.000297</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.19</td>                                                |
|      | <td>0.00045</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.00061</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2009.05.005">https://doi.org/10.1016/j.biomaterials.2009.05.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0028</td>                                              |
|      | <td>0.0000142</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6463/aa5bf6">https://doi.org/10.1088/1361-6463/aa5bf6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0003</td>                                              |
|      | <td>0.0001192</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6463/aa5bf6">https://doi.org/10.1088/1361-6463/aa5bf6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0003</td>                                              |
|      | <td>0.0000396</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6463/aa5bf6">https://doi.org/10.1088/1361-6463/aa5bf6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0012</td>                                              |
|      | <td>0.0000823</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6463/aa5bf6">https://doi.org/10.1088/1361-6463/aa5bf6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0052</td>                                              |
|      | <td>0.000239</td>                                            |
|      | <td><a href="https://doi.org/10.1088/1361-6463/aa5bf6">https://doi.org/10.1088/1361-6463/aa5bf6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.03</td>                                                |
|      | <td>0.000017</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.11.145">https://doi.org/10.1016/j.snb.2016.11.145</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>18.02</td>                                               |
|      | <td>0.000081</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.11.145">https://doi.org/10.1016/j.snb.2016.11.145</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeWO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.03</td>                                                |
|      | <td>0.0001225</td>                                           |
|      | <td><a href="https://doi.org/10.1002/smll.202003496">https://doi.org/10.1002/smll.202003496</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeWO4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.26</td>                                                |
|      | <td>0.00435</td>                                             |
|      | <td><a href="https://doi.org/10.1002/smll.202003496">https://doi.org/10.1002/smll.202003496</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0992</td>                                              |
|      | <td>0.00000156</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsanm.0c02807">https://doi.org/10.1021/acsanm.0c02807</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>114</td>                                                 |
|      | <td>0.00000197</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsanm.0c02807">https://doi.org/10.1021/acsanm.0c02807</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.18</td>                                                |
|      | <td>0.0012</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C6NR02730J">https://doi.org/10.1039/C6NR02730J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>1.5</td>                                                 |
|      | <td>0.000069</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6NR02730J">https://doi.org/10.1039/C6NR02730J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.025</td>                                               |
|      | <td>0.0000507</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5AY01732G">https://doi.org/10.1039/C5AY01732G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.0612</td>                                              |
|      | <td>0.000306</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2019.01.061">https://doi.org/10.1016/j.jcis.2019.01.061</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0963</td>                                              |
|      | <td>0.0000011</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2019.01.061">https://doi.org/10.1016/j.jcis.2019.01.061</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn2Fe2O5</td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.0342</td>                                              |
|      | <td>0.000244</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2019.01.061">https://doi.org/10.1016/j.jcis.2019.01.061</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn2Fe2O5</td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.0401</td>                                              |
|      | <td>0.00031</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2019.01.061">https://doi.org/10.1016/j.jcis.2019.01.061</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn2Fe2O5</td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.0486</td>                                              |
|      | <td>0.000625</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2019.01.061">https://doi.org/10.1016/j.jcis.2019.01.061</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.96</td>                                                |
|      | <td>0.00019</td>                                             |
|      | <td><a href="https://doi.org/10.1039/D0NR04177G">https://doi.org/10.1039/D0NR04177G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>26.64</td>                                               |
|      | <td>0.00006</td>                                             |
|      | <td><a href="https://doi.org/10.1039/D0NR04177G">https://doi.org/10.1039/D0NR04177G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.07</td>                                                |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D0NR04177G">https://doi.org/10.1039/D0NR04177G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.35</td>                                                |
|      | <td>0.00014</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2017.08.026">https://doi.org/10.1016/j.cej.2017.08.026</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.051</td>                                               |
|      | <td>0.000033</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jf500950p">https://doi.org/10.1021/jf500950p</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.037</td>                                               |
|      | <td>0.000032</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jf500950p">https://doi.org/10.1021/jf500950p</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>oxidase</td>                                             |
|      | <td>0.0006</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C8CC07062H">https://doi.org/10.1039/C8CC07062H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuCo2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.032</td>                                               |
|      | <td>0.000217</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.colsurfb.2019.110764">https://doi.org/10.1016/j.colsurfb.2019.110764</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnCo2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.009</td>                                               |
|      | <td>0.0000604</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.04.150">https://doi.org/10.1016/j.snb.2018.04.150</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.127</td>                                               |
|      | <td>0.00000999</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.aca.2016.11.035">https://doi.org/10.1016/j.aca.2016.11.035</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0469</td>                                              |
|      | <td>0.0459</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.bios.2020.112342">https://doi.org/10.1016/j.bios.2020.112342</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoO3</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>1.6769</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.aca.2020.01.035">https://doi.org/10.1016/j.aca.2020.01.035</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>3.8</td>                                                 |
|      | <td>0.0007</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>6.9</td>                                                 |
|      | <td>0.00036</td>                                             |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>2.4</td>                                                 |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>1.3</td>                                                 |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>1.9</td>                                                 |
|      | <td>0.0006</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>1.8</td>                                                 |
|      | <td>0.0005</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.8</td>                                                 |
|      | <td>0.0003</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.200805279">https://doi.org/10.1002/anie.200805279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.59</td>                                                |
|      | <td>0.00134</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C9NJ03527C">https://doi.org/10.1039/C9NJ03527C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>2.595</td>                                               |
|      | <td>0.00877</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C9NJ03527C">https://doi.org/10.1039/C9NJ03527C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>34.3</td>                                                |
|      | <td>0.0112</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.molcata.2013.05.016">https://doi.org/10.1016/j.molcata.2013.05.016</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>0.441</td>                                               |
|      | <td>0.0053</td>                                              |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>0.613</td>                                               |
|      | <td>0.0058</td>                                              |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>0.367</td>                                               |
|      | <td>0.0074</td>                                              |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>0.69</td>                                                |
|      | <td>0.0218</td>                                              |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>0.52</td>                                                |
|      | <td>0.1221</td>                                              |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuO2</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>3.59</td>                                                |
|      | <td>0.038167</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.0c07886">https://doi.org/10.1021/acsami.0c07886</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.198</td>                                               |
|      | <td>0.0000678</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2582-8">https://doi.org/10.1007/s00604-017-2582-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.38</td>                                                |
|      | <td>0.000241</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2582-8">https://doi.org/10.1007/s00604-017-2582-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.22</td>                                                |
|      | <td>0.000137</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.22</td>                                                |
|      | <td>0.000132</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.97</td>                                                |
|      | <td>0.000063</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>6.74</td>                                                |
|      | <td>0.000192</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.17</td>                                                |
|      | <td>0.000141</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.98</td>                                                |
|      | <td>0.000152</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.15</td>                                                |
|      | <td>0.000161</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>8.06</td>                                                |
|      | <td>0.000992</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7TB02676E">https://doi.org/10.1039/C7TB02676E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.086</td>                                               |
|      | <td>0.000132</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7NJ00899F">https://doi.org/10.1039/C7NJ00899F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.122</td>                                               |
|      | <td>0.000136</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7NJ00899F">https://doi.org/10.1039/C7NJ00899F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.047</td>                                               |
|      | <td>0.000178</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7NJ00899F">https://doi.org/10.1039/C7NJ00899F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.108</td>                                               |
|      | <td>0.000106</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C7NJ00899F">https://doi.org/10.1039/C7NJ00899F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co9S8</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.64</td>                                                |
|      | <td>0.00099</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.11.057">https://doi.org/10.1016/j.snb.2017.11.057</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co9S8</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>7.39</td>                                                |
|      | <td>0.00035</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.11.057">https://doi.org/10.1016/j.snb.2017.11.057</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mo0.1CeO2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.001</td>                                               |
|      | <td>0.00000964</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C7AY02459B">https://doi.org/10.1039/C7AY02459B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mo0.1CeO2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>8.85</td>                                                |
|      | <td>0.0000801</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7AY02459B">https://doi.org/10.1039/C7AY02459B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.623</td>                                               |
|      | <td>0.0000195</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7AY02459B">https://doi.org/10.1039/C7AY02459B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.067</td>                                               |
|      | <td>0.00000688</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C7AY02459B">https://doi.org/10.1039/C7AY02459B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO/Pt</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.33</td>                                                |
|      | <td>0.0002786</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2019.03.337">https://doi.org/10.1016/j.apsusc.2019.03.337</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO/Pt</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.75</td>                                                |
|      | <td>0.0001288</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2019.03.337">https://doi.org/10.1016/j.apsusc.2019.03.337</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.648</td>                                               |
|      | <td>0.0000596</td>                                           |
|      | <td><a href="[https://doi.org/10.1016/j.aca.2012.11.056  ](https://doi.org/10.1016/j.aca.2012.11.056)">https://doi.org/10.1016/j.aca.2012.11.056  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>29.16</td>                                               |
|      | <td>0.0000422</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.0c07886">https://doi.org/10.1021/acsami.0c07886</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu(OH)2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>1.335</td>                                               |
|      | <td>0.000421</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6TB01233G">https://doi.org/10.1039/C6TB01233G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu(OH)2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.379</td>                                               |
|      | <td>0.000391</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6TB01233G">https://doi.org/10.1039/C6TB01233G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.127</td>                                               |
|      | <td>0.00002</td>                                             |
|      | <td><a href="[https://doi.org/10.1016/j.snb.2017.07.108  ](https://doi.org/10.1016/j.snb.2017.07.108)">https://doi.org/10.1016/j.snb.2017.07.108  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1.14</td>                                                |
|      | <td>0.000031</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.snb.2017.07.108  ](https://doi.org/10.1016/j.snb.2017.07.108)">https://doi.org/10.1016/j.snb.2017.07.108  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.738</td>                                               |
|      | <td>0.0185</td>                                              |
|      | <td><a href="[https://doi.org/10.3390/s16040584 ](https://doi.org/10.3390/s16040584)">https://doi.org/10.3390/s16040584 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.232</td>                                               |
|      | <td>0.0129</td>                                              |
|      | <td><a href="[https://doi.org/10.3390/s16040584 ](https://doi.org/10.3390/s16040584)">https://doi.org/10.3390/s16040584 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Os</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.096</td>                                               |
|      | <td>0.000412</td>                                            |
|      | <td><a href="https://doi.org/10.1039/D0TA09247A">https://doi.org/10.1039/D0TA09247A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Os</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>3.88</td>                                                |
|      | <td>0.000565</td>                                            |
|      | <td><a href="https://doi.org/10.1039/D0TA09247A">https://doi.org/10.1039/D0TA09247A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu-CuFe2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.69</td>                                                |
|      | <td>0.0001687</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0DT02395G">https://doi.org/10.1039/D0DT02395G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu-CuFe2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.087</td>                                               |
|      | <td>0.0003218</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0DT02395G">https://doi.org/10.1039/D0DT02395G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru/C</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.071</td>                                               |
|      | <td>0.00002285</td>                                          |
|      | <td><a href="https://doi.org/10.1039/D0CC04101G">https://doi.org/10.1039/D0CC04101G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru/C</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.969</td>                                               |
|      | <td>0.0000179</td>                                           |
|      | <td><a href="[https://doi.org/10.1039/D0CC04101G ](https://doi.org/10.1039/D0CC04101G)">https://doi.org/10.1039/D0CC04101G </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0603</td>                                              |
|      | <td>0.000134</td>                                            |
|      | <td><a href="[https://doi.org/10.1007/s11434-016-1193-9  ](https://doi.org/10.1007/s11434-016-1193-9)">https://doi.org/10.1007/s11434-016-1193-9  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>318</td>                                                 |
|      | <td>0.0000741</td>                                           |
|      | <td><a href="[https://doi.org/10.1007/s11434-016-1193-9  ](https://doi.org/10.1007/s11434-016-1193-9)">https://doi.org/10.1007/s11434-016-1193-9  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.047</td>                                               |
|      | <td>0.00038</td>                                             |
|      | <td><a href="[https://doi.org/10.1007/s11434-016-1193-9  ](https://doi.org/10.1007/s11434-016-1193-9)">https://doi.org/10.1007/s11434-016-1193-9  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>730</td>                                                 |
|      | <td>0.00014</td>                                             |
|      | <td><a href="[https://doi.org/10.1007/s11434-016-1193-9  ](https://doi.org/10.1007/s11434-016-1193-9)">https://doi.org/10.1007/s11434-016-1193-9  </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0044</td>                                              |
|      | <td>0.000025</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-021-04942-7">https://doi.org/10.1007/s00604-021-04942-7</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>2.02</td>                                                |
|      | <td>0.00115</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsomega.0c00147">https://doi.org/10.1021/acsomega.0c00147</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>43.6</td>                                                |
|      | <td>0.000085</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsomega.0c00147">https://doi.org/10.1021/acsomega.0c00147</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.232</td>                                               |
|      | <td>0.0000456</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA18050G">https://doi.org/10.1039/C6RA18050G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.366</td>                                               |
|      | <td>0.0000476</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA18050G">https://doi.org/10.1039/C6RA18050G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe/CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.176</td>                                               |
|      | <td>0.000086</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6TB00422A">https://doi.org/10.1039/C6TB00422A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe/CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>47.6</td>                                                |
|      | <td>0.000166</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6TB00422A">https://doi.org/10.1039/C6TB00422A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.048</td>                                               |
|      | <td>0.0000037</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>2.79</td>                                                |
|      | <td>0.0000048</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiO2/TiN</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.083</td>                                               |
|      | <td>0.0000275</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiO2/TiN</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>4.96</td>                                                |
|      | <td>0.0000308</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiN</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.074</td>                                               |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiN</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>10.29</td>                                               |
|      | <td>0.0000784</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiN</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.034</td>                                               |
|      | <td>0.0000661</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiN</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>9.27</td>                                                |
|      | <td>0.0000556</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiN</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.091</td>                                               |
|      | <td>0.0000726</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiN</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>11.71</td>                                               |
|      | <td>0.0000567</td>                                           |
|      | <td><a href="https://doi.org/10.1002/anie.202106750">https://doi.org/10.1002/anie.202106750</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.06</td>                                                |
|      | <td>0.000041</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00153">https://doi.org/10.1021/acsanm.8b00153</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>14.8</td>                                                |
|      | <td>0.000006</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00153">https://doi.org/10.1021/acsanm.8b00153</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu-Fe4(Fe(CN)6)3</td>                                    |
|      | <td>peroxidase</td>                                          |
|      | <td>0.6</td>                                                 |
|      | <td>0.000179</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00216-021-03347-y">https://doi.org/10.1007/s00216-021-03347-y</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu-Fe4(Fe(CN)6)3</td>                                    |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.00012</td>                                             |
|      | <td><a href="https://doi.org/10.1007/s00216-021-03347-y">https://doi.org/10.1007/s00216-021-03347-y</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.02</td>                                                |
|      | <td>0.000108</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.5b01271">https://doi.org/10.1021/acsami.5b01271</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>266</td>                                                 |
|      | <td>0.000385</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.5b01271">https://doi.org/10.1021/acsami.5b01271</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.22</td>                                                |
|      | <td>0.000558</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2010.11.004">https://doi.org/10.1016/j.biomaterials.2010.11.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>187.25</td>                                              |
|      | <td>0.32</td>                                                |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2010.11.004">https://doi.org/10.1016/j.biomaterials.2010.11.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.236</td>                                               |
|      | <td>0.000006</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.201200643">https://doi.org/10.1002/chem.201200643</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>212</td>                                                 |
|      | <td>0.000135</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.201200643">https://doi.org/10.1002/chem.201200643</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.989</td>                                               |
|      | <td>0.000303333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>2.845</td>                                               |
|      | <td>0.000281667</td>                                         |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.26</td>                                                |
|      | <td>0.000236667</td>                                         |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.431</td>                                               |
|      | <td>0.000651667</td>                                         |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.19</td>                                                |
|      | <td>0.000908333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/chem.201800770">https://doi.org/10.1002/chem.201800770</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.196</td>                                               |
|      | <td>0.000933333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201708573">https://doi.org/10.1002/anie.201708573</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.16</td>                                                |
|      | <td>0.0013</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.201708573">https://doi.org/10.1002/anie.201708573</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.31</td>                                                |
|      | <td>0.0000821</td>                                           |
|      | <td><a href="[https://doi.org/10.1039/C2AN35700C ](https://doi.org/10.1039/C2AN35700C)">https://doi.org/10.1039/C2AN35700C </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.0000571</td>                                           |
|      | <td><a href="[https://doi.org/10.1039/C2AN35700C ](https://doi.org/10.1039/C2AN35700C)">https://doi.org/10.1039/C2AN35700C </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.1Au</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.113</td>                                               |
|      | <td>0.000018</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C2NR31716H">https://doi.org/10.1039/C2NR31716H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.1Au</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.436</td>                                               |
|      | <td>0.000000664</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C2NR31716H">https://doi.org/10.1039/C2NR31716H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5Ag0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.25</td>                                                |
|      | <td>0.0001057</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s12274-016-1395-0">https://doi.org/10.1007/s12274-016-1395-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5Ag0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.35</td>                                                |
|      | <td>0.0001596</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s12274-016-1395-0">https://doi.org/10.1007/s12274-016-1395-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5Ag0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.38</td>                                                |
|      | <td>0.0003304</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s12274-016-1395-0">https://doi.org/10.1007/s12274-016-1395-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5Ag0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.86</td>                                                |
|      | <td>0.0003475</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s12274-016-1395-0">https://doi.org/10.1007/s12274-016-1395-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.02</td>                                                |
|      | <td>0.0000291</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>76</td>                                                  |
|      | <td>0.00075</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@PtAg0.33</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.016</td>                                               |
|      | <td>0.0000176</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@PtAg0.33</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>92</td>                                                  |
|      | <td>0.00054</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@PtAg0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.01</td>                                                |
|      | <td>0.0000129</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@PtAg0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>111.8</td>                                               |
|      | <td>0.0005</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>180</td>                                                 |
|      | <td>0.00365</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsnano.1c03128">https://doi.org/10.1021/acsnano.1c03128</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir0.2Pt0.8</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.16</td>                                                |
|      | <td>0.00225</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2021.03.029">https://doi.org/10.1016/j.jtice.2021.03.029</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir0.2Pt0.8</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.75</td>                                                |
|      | <td>0.00266</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2021.03.029">https://doi.org/10.1016/j.jtice.2021.03.029</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.29</td>                                                |
|      | <td>0.000039</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.jcis.2017.11.064 ](https://doi.org/10.1016/j.jcis.2017.11.064)">https://doi.org/10.1016/j.jcis.2017.11.064 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>44.69</td>                                               |
|      | <td>0.0000223</td>                                           |
|      | <td><a href="[https://doi.org/10.1016/j.jcis.2017.11.064 ](https://doi.org/10.1016/j.jcis.2017.11.064)">https://doi.org/10.1016/j.jcis.2017.11.064 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/MoO3 </td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0352</td>                                              |
|      | <td>0.0000283</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB01337D">https://doi.org/10.1039/D0TB01337D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/MoO3 </td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.134</td>                                               |
|      | <td>0.0000291</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB01337D">https://doi.org/10.1039/D0TB01337D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.112</td>                                               |
|      | <td>0.0000047</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB01337D">https://doi.org/10.1039/D0TB01337D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.254</td>                                               |
|      | <td>0.00000389</td>                                          |
|      | <td><a href="https://doi.org/10.1039/D0TB01337D">https://doi.org/10.1039/D0TB01337D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag3PO4</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0923</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2018.07.073">https://doi.org/10.1016/j.talanta.2018.07.073</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3-Fe4(Fe(CN)6)3</td>                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.307</td>                                               |
|      | <td>0.00106</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C0JM00174K">https://doi.org/10.1039/C0JM00174K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3-Fe4(Fe(CN)6)4</td>                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>323.6</td>                                               |
|      | <td>0.00117</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C0JM00174K">https://doi.org/10.1039/C0JM00174K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3S4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.16</td>                                                |
|      | <td>0.00001146</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1690-6">https://doi.org/10.1007/s00604-015-1690-6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3S4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.158</td>                                               |
|      | <td>0.00002168</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1690-6">https://doi.org/10.1007/s00604-015-1690-6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.85</td>                                                |
|      | <td>0.0001331</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac300939z">https://doi.org/10.1021/ac300939z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>1.66</td>                                                |
|      | <td>0.0000774</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac300939z">https://doi.org/10.1021/ac300939z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.5Mn0.5Fe2O4</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>0.139</td>                                               |
|      | <td>0.0045</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2011.09.026">https://doi.org/10.1016/j.talanta.2011.09.026</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.5Mn0.5Fe2O4</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>310</td>                                                 |
|      | <td>0.00363</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2011.09.026">https://doi.org/10.1016/j.talanta.2011.09.026</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeSe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.04</td>                                                |
|      | <td>0.000089</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.07.070">https://doi.org/10.1016/j.snb.2012.07.070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeSe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>13.2</td>                                                |
|      | <td>0.000154</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.07.070">https://doi.org/10.1016/j.snb.2012.07.070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.08</td>                                                |
|      | <td>0.000073</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.07.070">https://doi.org/10.1016/j.snb.2012.07.070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>7.44</td>                                                |
|      | <td>0.000117</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.07.070">https://doi.org/10.1016/j.snb.2012.07.070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnSe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0348</td>                                              |
|      | <td>0.000734</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.materresbull.2015.03.018">https://doi.org/10.1016/j.materresbull.2015.03.018</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnSe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>87</td>                                                  |
|      | <td>0.0000478</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.materresbull.2015.03.018">https://doi.org/10.1016/j.materresbull.2015.03.018</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.007</td>                                               |
|      | <td>0.0000896</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2013.01.032">https://doi.org/10.1016/j.talanta.2013.01.032</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>12</td>                                                  |
|      | <td>0.000219</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2013.01.032">https://doi.org/10.1016/j.talanta.2013.01.032</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CdS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0095</td>                                              |
|      | <td>0.0000357</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.molcata.2012.03.007">https://doi.org/10.1016/j.molcata.2012.03.007</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CdS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>3.62</td>                                                |
|      | <td>0.000056</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.molcata.2012.03.007">https://doi.org/10.1016/j.molcata.2012.03.007</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@C</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0323</td>                                              |
|      | <td>0.0000863</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b17916">https://doi.org/10.1021/acsami.7b17916</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@C</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>210</td>                                                 |
|      | <td>0.00033</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.7b17916">https://doi.org/10.1021/acsami.7b17916</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuInS2</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>2.01</td>                                                |
|      | <td>0.0000978</td>                                           |
|      | <td><a href="[https://doi.org/10.1016/j.snb.2014.12.052    ](https://doi.org/10.1016/j.snb.2014.12.052 )">https://doi.org/10.1016/j.snb.2014.12.052    </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WC</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.274</td>                                               |
|      | <td>0.0000681</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2013.11.040">https://doi.org/10.1016/j.bios.2013.11.040</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WC</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>119.6</td>                                               |
|      | <td>0.0000716</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2013.11.040">https://doi.org/10.1016/j.bios.2013.11.040</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Si</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1.502</td>                                               |
|      | <td>0.0001472</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C4CC01703J">https://doi.org/10.1039/C4CC01703J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Si</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.065</td>                                               |
|      | <td>0.0000565</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C4CC01703J">https://doi.org/10.1039/C4CC01703J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CdS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0054</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apcatb.2012.07.005">https://doi.org/10.1016/j.apcatb.2012.07.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CdS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>6.54</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.apcatb.2012.07.005">https://doi.org/10.1016/j.apcatb.2012.07.005</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeP</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0653</td>                                              |
|      | <td>0.0000954</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2015.08.032">https://doi.org/10.1016/j.jcis.2015.08.032</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeP</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>2.907</td>                                               |
|      | <td>0.0000697</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2015.08.032">https://doi.org/10.1016/j.jcis.2015.08.032</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.094</td>                                               |
|      | <td>0.00146</td>                                             |
|      | <td><a href="https://doi.org/10.1021/jacs.6b07590">https://doi.org/10.1021/jacs.6b07590</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>272.78</td>                                              |
|      | <td>0.0027</td>                                              |
|      | <td><a href="https://doi.org/10.1021/jacs.6b07590">https://doi.org/10.1021/jacs.6b07590</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>92.19</td>                                               |
|      | <td>0.17152</td>                                             |
|      | <td><a href="https://doi.org/10.1021/jacs.6b07590">https://doi.org/10.1021/jacs.6b07590</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.543</td>                                               |
|      | <td>0.000452</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-016-1915-3">https://doi.org/10.1007/s00604-016-1915-3</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>32.87</td>                                               |
|      | <td>0.000434</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-016-1915-3">https://doi.org/10.1007/s00604-016-1915-3</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BN</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.157</td>                                               |
|      | <td>0.0001854</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA14856E">https://doi.org/10.1039/C6RA14856E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BN</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>10.88</td>                                               |
|      | <td>0.0001069</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA14856E">https://doi.org/10.1039/C6RA14856E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOBr</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.61</td>                                                |
|      | <td>0.0000263</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3NR06533B">https://doi.org/10.1039/C3NR06533B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOBr</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.046</td>                                               |
|      | <td>0.0000037</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3NR06533B">https://doi.org/10.1039/C3NR06533B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOCl</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0059</td>                                              |
|      | <td>0.00666</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C6QM00149A">https://doi.org/10.1039/C6QM00149A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOCl</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0006</td>                                              |
|      | <td>0.00246</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C6QM00149A">https://doi.org/10.1039/C6QM00149A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOBr</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0062</td>                                              |
|      | <td>0.00845</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C6QM00149A">https://doi.org/10.1039/C6QM00149A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOBr</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0004</td>                                              |
|      | <td>0.00249</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C6QM00149A">https://doi.org/10.1039/C6QM00149A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOI</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0313</td>                                              |
|      | <td>61</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C6QM00149A">https://doi.org/10.1039/C6QM00149A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOI</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0329</td>                                              |
|      | <td>27.6</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C6QM00149A">https://doi.org/10.1039/C6QM00149A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOI</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.024</td>                                               |
|      | <td>0.0000286</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA00368K">https://doi.org/10.1039/C6RA00368K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiOI</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0998</td>                                              |
|      | <td>0.0000735</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA00368K">https://doi.org/10.1039/C6RA00368K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co4N</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.243</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b09861">https://doi.org/10.1021/acsami.7b09861</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co4N</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>2.95</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b09861">https://doi.org/10.1021/acsami.7b09861</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoOOH</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>2.02</td>                                                |
|      | <td>0.0000474</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00216-017-0372-0">https://doi.org/10.1007/s00216-017-0372-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoOOH</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.06</td>                                                |
|      | <td>0.0000349</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00216-017-0372-0">https://doi.org/10.1007/s00216-017-0372-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu3(PO4)2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>35.18</td>                                               |
|      | <td>0.0000339</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5CC00040H">https://doi.org/10.1039/C5CC00040H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.75Se</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>12.6</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C6AY02275H">https://doi.org/10.1039/C6AY02275H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.75Se</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.58</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C6AY02275H">https://doi.org/10.1039/C6AY02275H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3(PO4)2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.36</td>                                                |
|      | <td>0.000158</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2018.01.080">https://doi.org/10.1016/j.talanta.2018.01.080</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3(PO4)2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.11</td>                                                |
|      | <td>0.000558</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2018.01.080">https://doi.org/10.1016/j.talanta.2018.01.080</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3(PO4)2(OH)2</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.055</td>                                               |
|      | <td>0.0001688</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8NJ00324F">https://doi.org/10.1039/C8NJ00324F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3(PO4)2(OH)2</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.47</td>                                                |
|      | <td>0.0000596</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8NJ00324F">https://doi.org/10.1039/C8NJ00324F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0082</td>                                              |
|      | <td>0.000087</td>                                            |
|      | <td><a href="https://doi.org/10.1021/am300408r">https://doi.org/10.1021/am300408r</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>9.36</td>                                                |
|      | <td>0.000192</td>                                            |
|      | <td><a href="https://doi.org/10.1021/am300408r">https://doi.org/10.1021/am300408r</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeSe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0089</td>                                              |
|      | <td>0.0000422</td>                                           |
|      | <td><a href="https://doi.org/10.1021/am300408r">https://doi.org/10.1021/am300408r</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeSe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>8.09</td>                                                |
|      | <td>0.0000651</td>                                           |
|      | <td><a href="https://doi.org/10.1021/am300408r">https://doi.org/10.1021/am300408r</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnOOH</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>2.182</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.jtice.2015.08.021">https://doi.org/10.1016/j.jtice.2015.08.021</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>KFePW12O40</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.346</td>                                               |
|      | <td>0.000037</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8DT01146J">https://doi.org/10.1039/C8DT01146J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>KFePW12O40</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>165</td>                                                 |
|      | <td>0.000069</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8DT01146J">https://doi.org/10.1039/C8DT01146J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoSe2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.014</td>                                               |
|      | <td>0.0000056</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7TB02434G">https://doi.org/10.1039/C7TB02434G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoSe2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.155</td>                                               |
|      | <td>0.0000099</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7TB02434G">https://doi.org/10.1039/C7TB02434G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WSe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.433</td>                                               |
|      | <td>0.0000143</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7NR03179C">https://doi.org/10.1039/C7NR03179C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WSe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>19.53</td>                                               |
|      | <td>0.0000222</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7NR03179C">https://doi.org/10.1039/C7NR03179C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1.047</td>                                               |
|      | <td>0.0000397</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5TB00684H">https://doi.org/10.1039/C5TB00684H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>31.265</td>                                              |
|      | <td>0.000264</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5TB00684H">https://doi.org/10.1039/C5TB00684H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.08</td>                                                |
|      | <td>0.000224</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5AN01103E">https://doi.org/10.1039/C5AN01103E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>137</td>                                                 |
|      | <td>0.000246</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5AN01103E">https://doi.org/10.1039/C5AN01103E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.068</td>                                               |
|      | <td>0.000315</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5AN01103E">https://doi.org/10.1039/C5AN01103E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>156</td>                                                 |
|      | <td>0.000408</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5AN01103E">https://doi.org/10.1039/C5AN01103E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.045</td>                                               |
|      | <td>0.000091</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5AN01103E">https://doi.org/10.1039/C5AN01103E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>254</td>                                                 |
|      | <td>0.000208</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C5AN01103E">https://doi.org/10.1039/C5AN01103E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.119</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.11.032">https://doi.org/10.1016/j.bios.2014.11.032</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>41.8</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.11.032">https://doi.org/10.1016/j.bios.2014.11.032</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.06Ag</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.396</td>                                               |
|      | <td>0.0000141</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2015.03.050">https://doi.org/10.1016/j.talanta.2015.03.050</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.06Ag</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>94.7</td>                                                |
|      | <td>0.0000292</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2015.03.050">https://doi.org/10.1016/j.talanta.2015.03.050</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiAu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0893</td>                                              |
|      | <td>0.000015</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C2CC32833J">https://doi.org/10.1039/C2CC32833J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiAu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.119</td>                                               |
|      | <td>0.000000725</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C2CC32833J">https://doi.org/10.1039/C2CC32833J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiAu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.377</td>                                               |
|      | <td>0.00000125</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C2CC32833J">https://doi.org/10.1039/C2CC32833J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BiAu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.07</td>                                                |
|      | <td>0.000000034</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C2CC32833J">https://doi.org/10.1039/C2CC32833J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.13</td>                                                |
|      | <td>0.000065</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>340</td>                                                 |
|      | <td>0.000051</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.054</td>                                               |
|      | <td>0.000097</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>700</td>                                                 |
|      | <td>0.000065</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.000085</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>180</td>                                                 |
|      | <td>0.000053</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.19</td>                                                |
|      | <td>0.000055</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>180</td>                                                 |
|      | <td>0.000029</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.5b03525">https://doi.org/10.1021/acsnano.5b03525</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.41</td>                                                |
|      | <td>0.0000582</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA16619A">https://doi.org/10.1039/C6RA16619A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>7.15</td>                                                |
|      | <td>0.0000265</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA16619A">https://doi.org/10.1039/C6RA16619A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.064</td>                                               |
|      | <td>0.000764</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.aca.2016.10.013 ](https://doi.org/10.1016/j.aca.2016.10.013)">https://doi.org/10.1016/j.aca.2016.10.013 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.753</td>                                               |
|      | <td>0.000237</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.aca.2016.10.013 ](https://doi.org/10.1016/j.aca.2016.10.013)">https://doi.org/10.1016/j.aca.2016.10.013 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.8S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>1.72</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C6AY03034C">https://doi.org/10.1039/C6AY03034C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.8S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>37.1</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C6AY03034C">https://doi.org/10.1039/C6AY03034C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.008</td>                                               |
|      | <td>0.000107</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apcata.2012.01.025">https://doi.org/10.1016/j.apcata.2012.01.025</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>7.67</td>                                                |
|      | <td>0.000207</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apcata.2012.01.025">https://doi.org/10.1016/j.apcata.2012.01.025</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.28</td>                                                |
|      | <td>0.000416</td>                                            |
|      | <td><a href="[https://doi.org/10.1007/s00604-017-2552-1 ](https://doi.org/10.1007/s00604-017-2552-1)">https://doi.org/10.1007/s00604-017-2552-1 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>3.49</td>                                                |
|      | <td>0.000557</td>                                            |
|      | <td><a href="[https://doi.org/10.1007/s00604-017-2552-1 ](https://doi.org/10.1007/s00604-017-2552-1)">https://doi.org/10.1007/s00604-017-2552-1 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.83</td>                                                |
|      | <td>0.0000431</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.001">https://doi.org/10.1016/j.bios.2014.07.001</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.24</td>                                                |
|      | <td>0.0000452</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.07.001">https://doi.org/10.1016/j.bios.2014.07.001</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0549</td>                                              |
|      | <td>0.00000048</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.05.069">https://doi.org/10.1016/j.snb.2017.05.069</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1724</td>                                              |
|      | <td>0.0001005</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.05.069">https://doi.org/10.1016/j.snb.2017.05.069</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgI</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0238</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/am501830v">https://doi.org/10.1021/am501830v</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AgI</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>2.86</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/am501830v">https://doi.org/10.1021/am501830v</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.216</td>                                               |
|      | <td>0.0002427</td>                                           |
|      | <td><a href="https://doi.org/10.1016/S1872-2040(17)61083-1">https://doi.org/10.1016/S1872-2040(17)61083-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.015</td>                                               |
|      | <td>0.0001513</td>                                           |
|      | <td><a href="https://doi.org/10.1016/S1872-2040(17)61083-1">https://doi.org/10.1016/S1872-2040(17)61083-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuCo2S4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>3.66</td>                                                |
|      | <td>0.0001084</td>                                           |
|      | <td><a href="https://doi.org/10.1002/cbic.202000066">https://doi.org/10.1002/cbic.202000066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuCo2S4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>209.9</td>                                               |
|      | <td>0.0002328</td>                                           |
|      | <td><a href="https://doi.org/10.1002/cbic.202000066">https://doi.org/10.1002/cbic.202000066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>5.28</td>                                                |
|      | <td>0.00006322</td>                                          |
|      | <td><a href="https://doi.org/10.1002/cbic.202000066">https://doi.org/10.1002/cbic.202000066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>264.1</td>                                               |
|      | <td>0.0001256</td>                                           |
|      | <td><a href="https://doi.org/10.1002/cbic.202000066">https://doi.org/10.1002/cbic.202000066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>3.13</td>                                                |
|      | <td>0.00003662</td>                                          |
|      | <td><a href="https://doi.org/10.1002/cbic.202000066">https://doi.org/10.1002/cbic.202000066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>114.5</td>                                               |
|      | <td>0.00005904</td>                                          |
|      | <td><a href="https://doi.org/10.1002/cbic.202000066">https://doi.org/10.1002/cbic.202000066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WSe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.205</td>                                               |
|      | <td>0.0000125</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D1NJ00819F">https://doi.org/10.1039/D1NJ00819F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WSe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.746</td>                                               |
|      | <td>0.00000484</td>                                          |
|      | <td><a href="https://doi.org/10.1039/D1NJ00819F">https://doi.org/10.1039/D1NJ00819F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaFeO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.427</td>                                               |
|      | <td>0.0007301</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2020.128642">https://doi.org/10.1016/j.snb.2020.128642</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaFeO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.209</td>                                               |
|      | <td>0.0017247</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2020.128642">https://doi.org/10.1016/j.snb.2020.128642</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2ZnSnSSe3</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.109</td>                                               |
|      | <td>0.000523</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-018-3185-8">https://doi.org/10.1007/s00604-018-3185-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2ZnSnSSe3</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.395</td>                                               |
|      | <td>0.000776</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-018-3185-8">https://doi.org/10.1007/s00604-018-3185-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.1-CdS</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.071</td>                                               |
|      | <td>0.00000931</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04451-z">https://doi.org/10.1007/s00604-020-04451-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.1-CdS</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>36.86</td>                                               |
|      | <td>0.00001026</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04451-z">https://doi.org/10.1007/s00604-020-04451-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoPW11O39</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.81</td>                                                |
|      | <td>0.000013</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8TB01853G">https://doi.org/10.1039/C8TB01853G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoPW11O39</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>2.01</td>                                                |
|      | <td>0.000617</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8TB01853G">https://doi.org/10.1039/C8TB01853G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.0000069</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00578">https://doi.org/10.1021/acsanm.8b00578</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1.52</td>                                                |
|      | <td>0.00396</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00578">https://doi.org/10.1021/acsanm.8b00578</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdCu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.25</td>                                                |
|      | <td>0.0000119</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00578">https://doi.org/10.1021/acsanm.8b00578</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdCu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>3.05</td>                                                |
|      | <td>0.00625</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00578">https://doi.org/10.1021/acsanm.8b00578</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>C</td>                                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.039</td>                                               |
|      | <td>0.0000361</td>                                           |
|      | <td><a href="[https://doi.org/10.1039/C1CC11943E ](https://doi.org/10.1039/C1CC11943E)">https://doi.org/10.1039/C1CC11943E </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>C</td>                                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>26.77</td>                                               |
|      | <td>0.0003061</td>                                           |
|      | <td><a href="[https://doi.org/10.1039/C1CC11943E ](https://doi.org/10.1039/C1CC11943E)">https://doi.org/10.1039/C1CC11943E </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.035</td>                                               |
|      | <td>0.00002</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C6RA23773H">https://doi.org/10.1039/C6RA23773H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>191</td>                                                 |
|      | <td>0.0000263</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA23773H">https://doi.org/10.1039/C6RA23773H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.023</td>                                               |
|      | <td>0.0000357</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA23773H">https://doi.org/10.1039/C6RA23773H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>130</td>                                                 |
|      | <td>0.0000405</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA23773H">https://doi.org/10.1039/C6RA23773H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.055</td>                                               |
|      | <td>0.0000213</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA23773H">https://doi.org/10.1039/C6RA23773H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>142</td>                                                 |
|      | <td>0.0000295</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA23773H">https://doi.org/10.1039/C6RA23773H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.052</td>                                               |
|      | <td>0.000164</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.langmuir.7b03430">https://doi.org/10.1021/acs.langmuir.7b03430</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>63.86</td>                                               |
|      | <td>0.00029</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acs.langmuir.7b03430">https://doi.org/10.1021/acs.langmuir.7b03430</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe4(Fe(CN)6)3</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>0.76</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1697-z">https://doi.org/10.1007/s00604-015-1697-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe4(Fe(CN)6)3</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>840</td>                                                 |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1697-z">https://doi.org/10.1007/s00604-015-1697-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe4(Fe(CN)6)3</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>0.337</td>                                               |
|      | <td>0.000216</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jacs.5b12070">https://doi.org/10.1021/jacs.5b12070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe4(Fe(CN)6)3</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>14.7</td>                                                |
|      | <td>0.000115</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jacs.5b12070">https://doi.org/10.1021/jacs.5b12070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe4(Fe(CN)6)3</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>1.08</td>                                                |
|      | <td>0.000314</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jacs.5b12070">https://doi.org/10.1021/jacs.5b12070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe4(Fe(CN)6)3</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>17.1</td>                                                |
|      | <td>0.000293</td>                                            |
|      | <td><a href="https://doi.org/10.1021/jacs.5b12070">https://doi.org/10.1021/jacs.5b12070</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.537</td>                                               |
|      | <td>0.000388</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.6b05810">https://doi.org/10.1021/acsnano.6b05810</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>2.812</td>                                               |
|      | <td>0.0000801</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsnano.6b05810">https://doi.org/10.1021/acsnano.6b05810</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1317</td>                                              |
|      | <td>0.03895</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.0c10981">https://doi.org/10.1021/acsami.0c10981</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>319.3</td>                                               |
|      | <td>0.06794</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.0c10981">https://doi.org/10.1021/acsami.0c10981</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.11</td>                                                |
|      | <td>0.00000038</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C8CC07800A">https://doi.org/10.1039/C8CC07800A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>101.8</td>                                               |
|      | <td>0.00000043</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C8CC07800A">https://doi.org/10.1039/C8CC07800A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.09</td>                                                |
|      | <td>0.000331</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8CC07800A">https://doi.org/10.1039/C8CC07800A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>103.2</td>                                               |
|      | <td>0.000382</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8CC07800A">https://doi.org/10.1039/C8CC07800A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>3</td>                                                   |
|      | <td>0.0000117</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8CC09799B">https://doi.org/10.1039/C8CC09799B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>29.79</td>                                               |
|      | <td>0.0000041</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8CC09799B">https://doi.org/10.1039/C8CC09799B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>C</td>                                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.427</td>                                               |
|      | <td>0.0000429</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.8b04067">https://doi.org/10.1021/acssuschemeng.8b04067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>C</td>                                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.244</td>                                               |
|      | <td>0.000222</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.8b04067">https://doi.org/10.1021/acssuschemeng.8b04067</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.433</td>                                               |
|      | <td>0.000121</td>                                            |
|      | <td><a href="https://doi.org/10.1039/D0TB00239A">https://doi.org/10.1039/D0TB00239A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.015</td>                                               |
|      | <td>0.0000144</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB00239A">https://doi.org/10.1039/D0TB00239A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.196</td>                                               |
|      | <td>0.0000962</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB00239A">https://doi.org/10.1039/D0TB00239A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.007</td>                                               |
|      | <td>0.0000202</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB00239A">https://doi.org/10.1039/D0TB00239A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.281</td>                                               |
|      | <td>0.0001037</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB00239A">https://doi.org/10.1039/D0TB00239A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.012</td>                                               |
|      | <td>0.0000143</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0TB00239A">https://doi.org/10.1039/D0TB00239A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.0101</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2019.120707">https://doi.org/10.1016/j.talanta.2019.120707</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn2O3</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.13</td>                                                |
|      | <td>0.00015</td>                                             |
|      | <td><a href="https://doi.org/10.1002/chem.202100567">https://doi.org/10.1002/chem.202100567</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.15</td>                                                |
|      | <td>0.000038</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.126876">https://doi.org/10.1016/j.snb.2019.126876</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdIr</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.28</td>                                                |
|      | <td>0.000079</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.9b04366">https://doi.org/10.1021/acsnano.9b04366</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Ir</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.22</td>                                                |
|      | <td>0.000031</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.9b04366">https://doi.org/10.1021/acsnano.9b04366</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.43</td>                                                |
|      | <td>0.000018</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsnano.9b04366">https://doi.org/10.1021/acsnano.9b04366</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.25Pt0.75</td>                                        |
|      | <td>oxidase</td>                                             |
|      | <td>0.058</td>                                               |
|      | <td>0.000114</td>                                            |
|      | <td><a href="https://doi.org/10.1039/c9tb00730j">https://doi.org/10.1039/c9tb00730j</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Se</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>8.3</td>                                                 |
|      | <td>0.0000507</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s11051-016-3357-6">https://doi.org/10.1007/s11051-016-3357-6</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.42</td>                                                |
|      | <td>0.0001004</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acssensors.6b00500">https://doi.org/10.1021/acssensors.6b00500</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.051</td>                                               |
|      | <td>0.0001087</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-017-1181-8">https://doi.org/10.1007/s10853-017-1181-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.7Se0.3</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.029</td>                                               |
|      | <td>0.0001948</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s10853-017-1181-8">https://doi.org/10.1007/s10853-017-1181-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuPt</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.29</td>                                                |
|      | <td>0.0000075</td>                                           |
|      | <td><a href="https://doi.org/10.1002/slct.201900681">https://doi.org/10.1002/slct.201900681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.0001</td>                                              |
|      | <td>0.00563</td>                                             |
|      | <td><a href="https://doi.org/10.1007/s12274-020-2680-5">https://doi.org/10.1007/s12274-020-2680-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.0035</td>                                              |
|      | <td>0.0168</td>                                              |
|      | <td><a href="https://doi.org/10.1007/s12274-020-2680-5">https://doi.org/10.1007/s12274-020-2680-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.0009</td>                                              |
|      | <td>0.00158</td>                                             |
|      | <td><a href="https://doi.org/10.1007/s12274-020-2680-5">https://doi.org/10.1007/s12274-020-2680-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.28</td>                                                |
|      | <td>0.0001365</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2326-9">https://doi.org/10.1007/s00604-017-2326-9</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Tb4O7</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.124</td>                                               |
|      | <td>0.0000431</td>                                           |
|      | <td><a href="https://doi.org/10.1186/s12951-019-0487-x">https://doi.org/10.1186/s12951-019-0487-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.0136</td>                                              |
|      | <td>0.000822</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2021.126585">https://doi.org/10.1016/j.colsurfa.2021.126585</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.0378</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/asia.201500942">https://doi.org/10.1002/asia.201500942</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.23</td>                                                |
|      | <td>0.000417</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s41664-019-00100-4">https://doi.org/10.1007/s41664-019-00100-4</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.102</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.3390/nano10061015">https://doi.org/10.3390/nano10061015</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>54.92</td>                                               |
|      | <td>0.0000095</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7RA10370K">https://doi.org/10.1039/C7RA10370K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.155</td>                                               |
|      | <td>0.000038885</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C7RA10370K">https://doi.org/10.1039/C7RA10370K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.75Pt0.25</td>                                        |
|      | <td>oxidase</td>                                             |
|      | <td>0.02</td>                                                |
|      | <td>0.000006</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep40103">https://doi.org/10.1038/srep40103</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.5Pt0.5</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.048</td>                                               |
|      | <td>0.000017</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep40103">https://doi.org/10.1038/srep40103</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.25Pt0.75</td>                                        |
|      | <td>oxidase</td>                                             |
|      | <td>0.16</td>                                                |
|      | <td>0.000173</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep40103">https://doi.org/10.1038/srep40103</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.15Pt0.85</td>                                        |
|      | <td>oxidase</td>                                             |
|      | <td>0.23</td>                                                |
|      | <td>0.000181</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep40103">https://doi.org/10.1038/srep40103</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.53</td>                                                |
|      | <td>0.000327</td>                                            |
|      | <td><a href="https://doi.org/10.1038/srep40103">https://doi.org/10.1038/srep40103</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.0544</td>                                              |
|      | <td>0.00579</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.5b05180">https://doi.org/10.1021/acsami.5b05180</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>4.73</td>                                                |
|      | <td>0.00068</td>                                             |
|      | <td><a href="[https://https://doi.org/10.1021/acsnano.9b04366](https://https//doi.org/10.1021/acsnano.9b04366)">https://https://doi.org/10.1021/acsnano.9b04366</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.17</td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.006</td>                                               |
|      | <td>0.0000262</td>                                           |
|      | <td><a href="[https://doi.org/10.1016/j.biomaterials.2010.09.040 ](https://doi.org/10.1016/j.biomaterials.2010.09.040)">https://doi.org/10.1016/j.biomaterials.2010.09.040 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.25</td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.013</td>                                               |
|      | <td>0.000025</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.biomaterials.2010.09.040 ](https://doi.org/10.1016/j.biomaterials.2010.09.040)">https://doi.org/10.1016/j.biomaterials.2010.09.040 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.17</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0095</td>                                              |
|      | <td>0.000102</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.biomaterials.2010.09.040 ](https://doi.org/10.1016/j.biomaterials.2010.09.040)">https://doi.org/10.1016/j.biomaterials.2010.09.040 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.25</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.027</td>                                               |
|      | <td>0.000181</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.biomaterials.2010.09.040 ](https://doi.org/10.1016/j.biomaterials.2010.09.040)">https://doi.org/10.1016/j.biomaterials.2010.09.040 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru0.1-V2O4</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.045</td>                                               |
|      | <td>0.000109</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.snb.2021.130266 ](https://doi.org/10.1016/j.snb.2021.130266)">https://doi.org/10.1016/j.snb.2021.130266 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru0.1-V2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.183</td>                                               |
|      | <td>0.000079</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.snb.2021.130266 ](https://doi.org/10.1016/j.snb.2021.130266)">https://doi.org/10.1016/j.snb.2021.130266 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru0.1-V2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.045</td>                                               |
|      | <td>0.000136</td>                                            |
|      | <td><a href="[https://doi.org/10.1016/j.snb.2021.130266 ](https://doi.org/10.1016/j.snb.2021.130266)">https://doi.org/10.1016/j.snb.2021.130266 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.38</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2021.126985">https://doi.org/10.1016/j.colsurfa.2021.126985</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0272</td>                                              |
|      | <td>0.0001267</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C9RA01227C">https://doi.org/10.1039/C9RA01227C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>129</td>                                                 |
|      | <td>232.8333333</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C5RA07636F">https://doi.org/10.1039/C5RA07636F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.2</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>6.7</td>                                                 |
|      | <td>165.1666667</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C5RA07636F">https://doi.org/10.1039/C5RA07636F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.2</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>651</td>                                                 |
|      | <td>739.6666667</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C5RA07636F">https://doi.org/10.1039/C5RA07636F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.0003</td>                                              |
|      | <td>no</td>                                                  |
|      | <td><a href="[https://doi.org/10.1016/j.aca.2015.04.052 ](https://doi.org/10.1016/j.aca.2015.04.052)">https://doi.org/10.1016/j.aca.2015.04.052 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.18</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="[https://doi.org/10.1016/j.aca.2015.04.052 ](https://doi.org/10.1016/j.aca.2015.04.052)">https://doi.org/10.1016/j.aca.2015.04.052 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.039</td>                                               |
|      | <td>0.00578</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C2AN35700C">https://doi.org/10.1039/C2AN35700C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0089</td>                                              |
|      | <td>0.0000177</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPtAg0.33</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.0065</td>                                              |
|      | <td>0.0000092</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPtAg0.5</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.0065</td>                                              |
|      | <td>0.0000056</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3RA23215H">https://doi.org/10.1039/C3RA23215H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag3PO4</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>0.136</td>                                               |
|      | <td>0.000893</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-020-04399-0">https://doi.org/10.1007/s00604-020-04399-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.018</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1039/C7NR03399K">https://doi.org/10.1039/C7NR03399K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.09</td>                                                |
|      | <td>0.007</td>                                               |
|      | <td><a href="[https://doi.org/10.1016/j.bios.2016.10.082 ](https://doi.org/10.1016/j.bios.2016.10.082)">https://doi.org/10.1016/j.bios.2016.10.082 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>TiO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.107</td>                                               |
|      | <td>0.0001565</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.5b02728">https://doi.org/10.1021/acs.analchem.5b02728</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@C</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.17</td>                                                |
|      | <td>0.0000492</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b17916">https://doi.org/10.1021/acsami.7b17916</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>24.7</td>                                                |
|      | <td>0.00238</td>                                             |
|      | <td><a href="https://doi.org/10.1021/am406033q">https://doi.org/10.1021/am406033q</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>4.82</td>                                                |
|      | <td>0.00189</td>                                             |
|      | <td><a href="https://doi.org/10.1021/am406033q">https://doi.org/10.1021/am406033q</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>63.9</td>                                                |
|      | <td>0.00123</td>                                             |
|      | <td><a href="https://doi.org/10.1021/am406033q">https://doi.org/10.1021/am406033q</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>458.9</td>                                               |
|      | <td>0.00000306</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C6CC08542C">https://doi.org/10.1039/C6CC08542C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>226.6</td>                                               |
|      | <td>0.00000445</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C6CC08542C">https://doi.org/10.1039/C6CC08542C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>37.99</td>                                               |
|      | <td>0.00000528</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C6CC08542C">https://doi.org/10.1039/C6CC08542C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ir</td>                                                  |
|      | <td>catalase</td>                                            |
|      | <td>297</td>                                                 |
|      | <td>0.54</td>                                                |
|      | <td><a href="https://doi.org/10.1021/acsami.5b01271">https://doi.org/10.1021/acsami.5b01271</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>catalase</td>                                            |
|      | <td>420.6</td>                                               |
|      | <td>0.84</td>                                                |
|      | <td><a href="https://doi.org/10.1016/j.biomaterials.2010.11.004">https://doi.org/10.1016/j.biomaterials.2010.11.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuO2</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>400</td>                                                 |
|      | <td>0.968</td>                                               |
|      | <td><a href="https://doi.org/10.1002/chem.201200643">https://doi.org/10.1002/chem.201200643</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>0.511</td>                                               |
|      | <td>0.122166667</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201708573">https://doi.org/10.1002/anie.201708573</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>catalase</td>                                            |
|      | <td>34.58</td>                                               |
|      | <td>0.00233</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsnano.1c03128">https://doi.org/10.1021/acsnano.1c03128</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoO2.8</td>                                              |
|      | <td>catalase</td>                                            |
|      | <td>6.72</td>                                                |
|      | <td>0.0196</td>                                              |
|      | <td><a href="[https://doi.org/10.1016/j.jcis.2018.12.093 ](https://doi.org/10.1016/j.jcis.2018.12.093)">https://doi.org/10.1016/j.jcis.2018.12.093 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O2S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.034</td>                                               |
|      | <td>0.522</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O2S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>30.11</td>                                               |
|      | <td>1.809</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O2S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.683</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O2S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>142.34</td>                                              |
|      | <td>4.488</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O2S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.182</td>                                               |
|      | <td>0.679</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O2S</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>195.48</td>                                              |
|      | <td>3.82</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.27</td>                                                |
|      | <td>0.787</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Eu2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>211.59</td>                                              |
|      | <td>4.366</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C5NJ02705E">https://doi.org/10.1039/C5NJ02705E</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuSe2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.207</td>                                               |
|      | <td>0.00072411</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s41664-019-00104-0">https://doi.org/10.1007/s41664-019-00104-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuSe2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.936</td>                                               |
|      | <td>0.00013193</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s41664-019-00104-0">https://doi.org/10.1007/s41664-019-00104-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuSe2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>2.22</td>                                                |
|      | <td>0.00032446</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s41664-019-00104-0">https://doi.org/10.1007/s41664-019-00104-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuSe2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.645</td>                                               |
|      | <td>0.00004234</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s41664-019-00104-0">https://doi.org/10.1007/s41664-019-00104-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>YVO4</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1062</td>                                              |
|      | <td>0.000361</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2021.126427">https://doi.org/10.1016/j.colsurfa.2021.126427</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>YVO4</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>3.82</td>                                                |
|      | <td>0.000597</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2021.126427">https://doi.org/10.1016/j.colsurfa.2021.126427</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce2(WO4)3</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.053</td>                                               |
|      | <td>0.0001709</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.saa.2020.118499">https://doi.org/10.1016/j.saa.2020.118499</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce2(WO4)3</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>4.25</td>                                                |
|      | <td>0.0002006</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.saa.2020.118499">https://doi.org/10.1016/j.saa.2020.118499</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mo5N6</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.456</td>                                               |
|      | <td>0.0000595</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-021-05112-5">https://doi.org/10.1007/s00604-021-05112-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mo5N6</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.082</td>                                               |
|      | <td>0.000009</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-021-05112-5">https://doi.org/10.1007/s00604-021-05112-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.409</td>                                               |
|      | <td>0.0000632</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122594">https://doi.org/10.1016/j.talanta.2021.122594</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.406</td>                                               |
|      | <td>0.0000549</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122594">https://doi.org/10.1016/j.talanta.2021.122594</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>catalase</td>                                            |
|      | <td>5.47</td>                                                |
|      | <td>0.00418</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122594">https://doi.org/10.1016/j.talanta.2021.122594</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.17</td>                                                |
|      | <td>0.0000281</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.127106">https://doi.org/10.1016/j.snb.2019.127106</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.42</td>                                                |
|      | <td>0.0000285</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.127106">https://doi.org/10.1016/j.snb.2019.127106</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.25</td>                                                |
|      | <td>0.0000185</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.127106">https://doi.org/10.1016/j.snb.2019.127106</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>5.17</td>                                                |
|      | <td>0.0000179</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.127106">https://doi.org/10.1016/j.snb.2019.127106</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.8Ni0.2S2</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.221</td>                                               |
|      | <td>0.000219</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.8Ni0.2S2</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0192</td>                                              |
|      | <td>0.000241</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.6Ni0.4S2</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.797</td>                                               |
|      | <td>0.000172</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.6Ni0.4S2</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.123</td>                                               |
|      | <td>0.000172</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.4Ni0.6S2</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.916</td>                                               |
|      | <td>0.000102</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.4Ni0.6S2</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.252</td>                                               |
|      | <td>0.000145</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.08</td>                                                |
|      | <td>0.000478</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0907</td>                                              |
|      | <td>0.000127</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.jpcc.1c10325">https://doi.org/10.1021/acs.jpcc.1c10325</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu9S8</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.66</td>                                                |
|      | <td>0.00000716</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.jpcs.2021.110534">https://doi.org/10.1016/j.jpcs.2021.110534</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu9S8</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.449</td>                                               |
|      | <td>0.00000851</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.jpcs.2021.110534">https://doi.org/10.1016/j.jpcs.2021.110534</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3016</td>                                              |
|      | <td>0.00003109</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.9b04043">https://doi.org/10.1021/acssuschemeng.9b04043</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.308</td>                                               |
|      | <td>0.000091533</td>                                         |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.9b04043">https://doi.org/10.1021/acssuschemeng.9b04043</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Bi2Fe4O9</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.07</td>                                                |
|      | <td>0.0000217</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2022.01.041">https://doi.org/10.1016/j.jcis.2022.01.041</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Bi2Fe4O9</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.73</td>                                                |
|      | <td>0.0000156</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2022.01.041">https://doi.org/10.1016/j.jcis.2022.01.041</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.17</td>                                                |
|      | <td>0.0000393</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2019.111983">https://doi.org/10.1016/j.bios.2019.111983</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3</td>                                                 |
|      | <td>0.0000562</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2019.111983">https://doi.org/10.1016/j.bios.2019.111983</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.43</td>                                                |
|      | <td>0.000002</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.nantod.2022.101421">https://doi.org/10.1016/j.nantod.2022.101421</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>13.17</td>                                               |
|      | <td>0.00001</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.nantod.2022.101421">https://doi.org/10.1016/j.nantod.2022.101421</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WSe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.32</td>                                                |
|      | <td>0.0000103</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.nantod.2022.101421">https://doi.org/10.1016/j.nantod.2022.101421</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WSe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>5.63</td>                                                |
|      | <td>0.000006</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.nantod.2022.101421">https://doi.org/10.1016/j.nantod.2022.101421</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WTe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.22</td>                                                |
|      | <td>0.0001538</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.nantod.2022.101421">https://doi.org/10.1016/j.nantod.2022.101421</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WTe2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.31</td>                                                |
|      | <td>0.000155</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.nantod.2022.101421">https://doi.org/10.1016/j.nantod.2022.101421</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeCoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.012</td>                                               |
|      | <td>0.0000107</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121142">https://doi.org/10.1016/j.talanta.2020.121142</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeCoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>18.64</td>                                               |
|      | <td>0.0000291</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2020.121142">https://doi.org/10.1016/j.talanta.2020.121142</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.049</td>                                               |
|      | <td>0.00002606</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C7NJ00292K">https://doi.org/10.1039/C7NJ00292K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.7414</td>                                              |
|      | <td>0.000015459</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C7NJ00292K">https://doi.org/10.1039/C7NJ00292K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0603</td>                                              |
|      | <td>0.00002077</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C7NJ00292K">https://doi.org/10.1039/C7NJ00292K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.927</td>                                               |
|      | <td>0.00001743</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C7NJ00292K">https://doi.org/10.1039/C7NJ00292K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2MoS4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>1.36</td>                                                |
|      | <td>0.0002729</td>                                           |
|      | <td><a href="https://doi.org/10.1002/smll.202001099">https://doi.org/10.1002/smll.202001099</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2MoS4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>25.46</td>                                               |
|      | <td>0.0004281</td>                                           |
|      | <td><a href="https://doi.org/10.1002/smll.202001099">https://doi.org/10.1002/smll.202001099</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2MoS4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.0121</td>                                              |
|      | <td>0.00011</td>                                             |
|      | <td><a href="https://doi.org/10.1002/smll.202001099">https://doi.org/10.1002/smll.202001099</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2411</td>                                              |
|      | <td>0.00065</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41596-018-0001-1">https://doi.org/10.1038/s41596-018-0001-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1277</td>                                              |
|      | <td>0.000275</td>                                            |
|      | <td><a href="https://doi.org/10.1038/s41596-018-0001-1">https://doi.org/10.1038/s41596-018-0001-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>C</td>                                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1037</td>                                              |
|      | <td>0.000562</td>                                            |
|      | <td><a href="https://doi.org/10.1038/s41596-018-0001-1">https://doi.org/10.1038/s41596-018-0001-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.027</td>                                               |
|      | <td>0.000113</td>                                            |
|      | <td><a href="https://doi.org/10.1080/03067319.2019.1599875">https://doi.org/10.1080/03067319.2019.1599875</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.03</td>                                                |
|      | <td>0.000046</td>                                            |
|      | <td><a href="https://doi.org/10.1080/03067319.2019.1599875">https://doi.org/10.1080/03067319.2019.1599875</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnOOH</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.037</td>                                               |
|      | <td>0.000087</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.04.020">https://doi.org/10.1016/j.snb.2019.04.020</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3V2O8</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.179</td>                                               |
|      | <td>0.000578</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apcatb.2019.118256">https://doi.org/10.1016/j.apcatb.2019.118256</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3V2O8</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.000053</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apcatb.2019.118256">https://doi.org/10.1016/j.apcatb.2019.118256</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3V2O8</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.444</td>                                               |
|      | <td>0.000095</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apcatb.2019.118256">https://doi.org/10.1016/j.apcatb.2019.118256</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4@NiO</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.036</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2018.01.019">https://doi.org/10.1016/j.talanta.2018.01.019</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4@NiO</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>8.17</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2018.01.019">https://doi.org/10.1016/j.talanta.2018.01.019</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiW12@Co3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.023</td>                                               |
|      | <td>0.000053</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C9AN01262A">https://doi.org/10.1039/C9AN01262A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiW12@Co3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>167.8</td>                                               |
|      | <td>0.000251</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C9AN01262A">https://doi.org/10.1039/C9AN01262A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mo0.02-Co3O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0558</td>                                              |
|      | <td>0.0000954</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00945">https://doi.org/10.1021/acsanm.8b00945</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mo0.02-Co3O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>22.48</td>                                               |
|      | <td>0.00005245</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00945">https://doi.org/10.1021/acsanm.8b00945</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0025</td>                                              |
|      | <td>0.0000623</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2011.02.014">https://doi.org/10.1016/j.bios.2011.02.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>25.3</td>                                                |
|      | <td>0.0000721</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2011.02.014">https://doi.org/10.1016/j.bios.2011.02.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.13</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/chem.200802158">https://doi.org/10.1002/chem.200802158</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>7.2</td>                                                 |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1002/chem.200802158">https://doi.org/10.1002/chem.200802158</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.525</td>                                               |
|      | <td>0.0000429</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C4NR03393K">https://doi.org/10.1039/C4NR03393K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0116</td>                                              |
|      | <td>0.0000516</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C4NR03393K">https://doi.org/10.1039/C4NR03393K</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.5Co0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>1.79</td>                                                |
|      | <td>0.000456</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C3CC41569D">https://doi.org/10.1039/C3CC41569D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.5Co0.5</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.06</td>                                                |
|      | <td>0.000132</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C3CC41569D">https://doi.org/10.1039/C3CC41569D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.38</td>                                                |
|      | <td>0.000238</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C3CC41569D">https://doi.org/10.1039/C3CC41569D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.32</td>                                                |
|      | <td>0.00041</td>                                             |
|      | <td><a href="[https://https://doi.org/10.1039/C3CC41569D](https://https//doi.org/10.1039/C3CC41569D)">https://https://doi.org/10.1039/C3CC41569D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>5.09</td>                                                |
|      | <td>0.0000998</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3CC41569D">https://doi.org/10.1039/C3CC41569D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1.14</td>                                                |
|      | <td>0.0000172</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C3CC41569D">https://doi.org/10.1039/C3CC41569D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>27.5</td>                                                |
|      | <td>0.000104</td>                                            |
|      | <td><a href="https://doi.org/10.1002/aoc.4465">https://doi.org/10.1002/aoc.4465</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>32.7</td>                                                |
|      | <td>0.000078</td>                                            |
|      | <td><a href="https://doi.org/10.1002/aoc.4465">https://doi.org/10.1002/aoc.4465</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>8.4</td>                                                 |
|      | <td>0.0000086</td>                                           |
|      | <td><a href="https://doi.org/10.1002/aoc.4465">https://doi.org/10.1002/aoc.4465</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>22.6</td>                                                |
|      | <td>0.0000082</td>                                           |
|      | <td><a href="https://doi.org/10.1002/aoc.4465">https://doi.org/10.1002/aoc.4465</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.264</td>                                               |
|      | <td>0.0001256</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s12274-018-2154-1">https://doi.org/10.1007/s12274-018-2154-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>4.51</td>                                                |
|      | <td>0.0006809</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s12274-018-2154-1">https://doi.org/10.1007/s12274-018-2154-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.485</td>                                               |
|      | <td>0.0000563</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.matlet.2013.04.020">https://doi.org/10.1016/j.matlet.2013.04.020</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1175.3</td>                                              |
|      | <td>0.0002396</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.matlet.2013.04.020">https://doi.org/10.1016/j.matlet.2013.04.020</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Pt0.15</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.147</td>                                               |
|      | <td>0.0000711</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.matlet.2013.04.020">https://doi.org/10.1016/j.matlet.2013.04.020</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Pt0.15</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>702.6</td>                                               |
|      | <td>0.0007136</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.matlet.2013.04.020">https://doi.org/10.1016/j.matlet.2013.04.020</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.63</td>                                                |
|      | <td>0.0027</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C3NR06896J">https://doi.org/10.1039/C3NR06896J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiAu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0411</td>                                              |
|      | <td>0.0001266</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adma.201405105">https://doi.org/10.1002/adma.201405105</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiAu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>15.81</td>                                               |
|      | <td>0.000173</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adma.201405105">https://doi.org/10.1002/adma.201405105</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiAu</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.2248</td>                                              |
|      | <td>0.0001187</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adma.201405105">https://doi.org/10.1002/adma.201405105</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt0.16</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.0154</td>                                              |
|      | <td>0.000008333</td>                                         |
|      | <td><a href="https://doi.org/10.1021/la104566e">https://doi.org/10.1021/la104566e</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pd0.2Pt</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.0132</td>                                              |
|      | <td>0.00001</td>                                             |
|      | <td><a href="https://doi.org/10.1021/la104566e">https://doi.org/10.1021/la104566e</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@PdPt</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.0112</td>                                              |
|      | <td>0.000011667</td>                                         |
|      | <td><a href="https://doi.org/10.1021/la104566e">https://doi.org/10.1021/la104566e</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.173</td>                                               |
|      | <td>0.000333</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.201101191">https://doi.org/10.1002/chem.201101191</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>185</td>                                                 |
|      | <td>0.486</td>                                               |
|      | <td><a href="https://doi.org/10.1002/chem.201101191">https://doi.org/10.1002/chem.201101191</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Si-Fe3O4</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.193</td>                                               |
|      | <td>0.000172</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.201101191">https://doi.org/10.1002/chem.201101191</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Si-Fe3O4</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>273</td>                                                 |
|      | <td>0.282</td>                                               |
|      | <td><a href="https://doi.org/10.1002/chem.201101191">https://doi.org/10.1002/chem.201101191</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Se</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.859</td>                                               |
|      | <td>0.000005333</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.bej.2019.107384">https://doi.org/10.1016/j.bej.2019.107384</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Se</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.852</td>                                               |
|      | <td>0.000023833</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.bej.2019.107384">https://doi.org/10.1016/j.bej.2019.107384</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3Fe</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.05</td>                                                |
|      | <td>0.000387</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C2TB00389A">https://doi.org/10.1039/C2TB00389A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3Fe</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.218</td>                                               |
|      | <td>0.000263</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C2TB00389A">https://doi.org/10.1039/C2TB00389A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>101.4</td>                                               |
|      | <td>0.043</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C6CC08542C">https://doi.org/10.1039/C6CC08542C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>676</td>                                                 |
|      | <td>0.83</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C6CC08542C">https://doi.org/10.1039/C6CC08542C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>589</td>                                                 |
|      | <td>0.361</td>                                               |
|      | <td><a href="https://doi.org/10.1039/C6CC08542C">https://doi.org/10.1039/C6CC08542C</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni@Pt</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.021</td>                                               |
|      | <td>0.000306</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.2c05425">https://doi.org/10.1021/acs.analchem.2c05425</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.0285</td>                                              |
|      | <td>0.0001406</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.2c05425">https://doi.org/10.1021/acs.analchem.2c05425</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtNi0.33</td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.0541</td>                                              |
|      | <td>0.0001956</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.2c05425">https://doi.org/10.1021/acs.analchem.2c05425</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtNi1</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0213</td>                                              |
|      | <td>0.0003059</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.2c05425">https://doi.org/10.1021/acs.analchem.2c05425</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtNi1</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0223</td>                                              |
|      | <td>0.0000788</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.2c05425">https://doi.org/10.1021/acs.analchem.2c05425</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>4.88</td>                                                |
|      | <td>0.000699</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.0c12593">https://doi.org/10.1021/acsami.0c12593</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.227</td>                                               |
|      | <td>0.000392</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.0c12593">https://doi.org/10.1021/acsami.0c12593</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(FeS2)0.3-SiO2</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.948</td>                                               |
|      | <td>0.00031</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsami.0c12593">https://doi.org/10.1021/acsami.0c12593</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(FeS2)0.3-SiO2</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0126</td>                                              |
|      | <td>0.000181</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsami.0c12593">https://doi.org/10.1021/acsami.0c12593</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.241</td>                                               |
|      | <td>0.0000509</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00216-018-1423-x">https://doi.org/10.1007/s00216-018-1423-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.347</td>                                               |
|      | <td>0.0000534</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00216-018-1423-x">https://doi.org/10.1007/s00216-018-1423-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2-C</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.16</td>                                                |
|      | <td>0.0000623</td>                                           |
|      | <td><a href="https://pubs.acs.org/doi/10.1021/acsabm.0c00605">https://pubs.acs.org/doi/10.1021/acsabm.0c00605</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>FeS2-C</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.46</td>                                                |
|      | <td>0.0001193</td>                                           |
|      | <td><a href="https://pubs.acs.org/doi/10.1021/acsabm.0c00606">https://pubs.acs.org/doi/10.1021/acsabm.0c00606</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu5ZnFe5S6</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>2.2</td>                                                 |
|      | <td>0.39</td>                                                |
|      | <td><a href="https://doi.org/10.1039/C5NR01728A">https://doi.org/10.1039/C5NR01728A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu5ZnFe5S6</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.07</td>                                                |
|      | <td>0.0056</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C5NR01728A">https://doi.org/10.1039/C5NR01728A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.045</td>                                               |
|      | <td>0.00000696</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-019-3395-8">https://doi.org/10.1007/s00604-019-3395-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.164</td>                                               |
|      | <td>0.00000899</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-019-3395-8">https://doi.org/10.1007/s00604-019-3395-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.025</td>                                               |
|      | <td>0.00009409</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C8NJ01190G">https://doi.org/10.1039/C8NJ01190G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.811</td>                                               |
|      | <td>0.00005139</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C8NJ01190G">https://doi.org/10.1039/C8NJ01190G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.83</td>                                                |
|      | <td>0.0000431</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5AN00031A">https://doi.org/10.1039/C5AN00031A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.24</td>                                                |
|      | <td>0.0000452</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5AN00031A">https://doi.org/10.1039/C5AN00031A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.467</td>                                               |
|      | <td>0.0000645</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5AN00031A">https://doi.org/10.1039/C5AN00031A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.926</td>                                               |
|      | <td>0.0000257</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5AN00031A">https://doi.org/10.1039/C5AN00031A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.41</td>                                                |
|      | <td>0.000474</td>                                            |
|      | <td><a href="https://doi.org/10.1002/ppsc.201500043">https://doi.org/10.1002/ppsc.201500043</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>12.8</td>                                                |
|      | <td>0.000151</td>                                            |
|      | <td><a href="https://doi.org/10.1002/ppsc.201500043">https://doi.org/10.1002/ppsc.201500043</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0603</td>                                              |
|      | <td>0.00002077</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.msec.2014.04.038">https://doi.org/10.1016/j.msec.2014.04.038</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.927</td>                                               |
|      | <td>0.0001908</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.msec.2014.04.038">https://doi.org/10.1016/j.msec.2014.04.038</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.439</td>                                               |
|      | <td>0.00001743</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.msec.2014.04.038">https://doi.org/10.1016/j.msec.2014.04.038</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.919</td>                                               |
|      | <td>0.00001075</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.msec.2014.04.038">https://doi.org/10.1016/j.msec.2014.04.038</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>108</td>                                                 |
|      | <td>0.00000284</td>                                          |
|      | <td><a href="https://doi.org/10.1002/crat.201300440">https://doi.org/10.1002/crat.201300440</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>117</td>                                                 |
|      | <td>0.00000363</td>                                          |
|      | <td><a href="https://doi.org/10.1002/crat.201300440">https://doi.org/10.1002/crat.201300440</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag@Fe3O4</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>75.2</td>                                                |
|      | <td>0.0000228</td>                                           |
|      | <td><a href="https://doi.org/10.1002/crat.201300440">https://doi.org/10.1002/crat.201300440</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag@Fe3O4</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>3.46</td>                                                |
|      | <td>0.0000228</td>                                           |
|      | <td><a href="https://doi.org/10.1002/crat.201300440">https://doi.org/10.1002/crat.201300440</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.005</td>                                               |
|      | <td>0.155</td>                                               |
|      | <td><a href="https://doi.org/10.1155/2019/5416963">https://doi.org/10.1155/2019/5416963</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>15.158</td>                                              |
|      | <td>0.0006523</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.aca.2020.01.043">https://doi.org/10.1016/j.aca.2020.01.043</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>WS2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.805</td>                                               |
|      | <td>0.00022</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.aca.2020.01.043">https://doi.org/10.1016/j.aca.2020.01.043</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoO3</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.093</td>                                               |
|      | <td>0.00003041</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoO3</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>109.5</td>                                               |
|      | <td>0.00005284</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.301</td>                                               |
|      | <td>0.00004252</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>6.1</td>                                                 |
|      | <td>0.00003611</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5-MoO3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.296</td>                                               |
|      | <td>0.00004263</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5-MoO3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>5.9</td>                                                 |
|      | <td>0.00003625</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5-MoO3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.106</td>                                               |
|      | <td>0.00004286</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.5-MoO3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>3.2</td>                                                 |
|      | <td>0.00003794</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4NR04115A">https://doi.org/10.1039/C4NR04115A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.8246</td>                                              |
|      | <td>0.00001161</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.0c01789">https://doi.org/10.1021/acsami.0c01789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>2.0828</td>                                              |
|      | <td>0.00001346</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.0c01789">https://doi.org/10.1021/acsami.0c01789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>N0.1-MoS2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.7916</td>                                              |
|      | <td>0.00001796</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.0c01789">https://doi.org/10.1021/acsami.0c01789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>N0.1-MoS2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.4459</td>                                              |
|      | <td>0.00004348</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.0c01789">https://doi.org/10.1021/acsami.0c01789</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(PtFe)0.5@Fe3O4</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>0.213</td>                                               |
|      | <td>0.00005477</td>                                          |
|      | <td><a href="https://doi.org/10.1002/ange.201904751">https://doi.org/10.1002/ange.201904751</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(PtFe)0.5@Fe3O4</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>53.55</td>                                               |
|      | <td>0.0001078</td>                                           |
|      | <td><a href="https://doi.org/10.1002/ange.201904751">https://doi.org/10.1002/ange.201904751</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.237</td>                                               |
|      | <td>0.0000602</td>                                           |
|      | <td><a href="https://doi.org/10.1002/ange.201904751">https://doi.org/10.1002/ange.201904751</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>217.6</td>                                               |
|      | <td>0.00008182</td>                                          |
|      | <td><a href="https://doi.org/10.1002/ange.201904751">https://doi.org/10.1002/ange.201904751</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.269</td>                                               |
|      | <td>0.00004477</td>                                          |
|      | <td><a href="https://doi.org/10.1002/ange.201904751">https://doi.org/10.1002/ange.201904751</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>120</td>                                                 |
|      | <td>0.00004598</td>                                          |
|      | <td><a href="https://doi.org/10.1002/ange.201904751">https://doi.org/10.1002/ange.201904751</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.49</td>                                                |
|      | <td>0.00016</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C8TB01948G">https://doi.org/10.1039/C8TB01948G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.9</td>                                                 |
|      | <td>0.000127</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8TB01948G">https://doi.org/10.1039/C8TB01948G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.0000021</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adfm.201801484">https://doi.org/10.1002/adfm.201801484</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1</td>                                                   |
|      | <td>0.0000018</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adfm.201801484">https://doi.org/10.1002/adfm.201801484</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt </td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.43</td>                                                |
|      | <td>0.000051</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adfm.201801484">https://doi.org/10.1002/adfm.201801484</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt </td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>14</td>                                                  |
|      | <td>0.00009</td>                                             |
|      | <td><a href="https://doi.org/10.1002/adfm.201801484">https://doi.org/10.1002/adfm.201801484</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.81</td>                                                |
|      | <td>0.00012</td>                                             |
|      | <td><a href="https://doi.org/10.1002/adfm.201801484">https://doi.org/10.1002/adfm.201801484</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>6.9</td>                                                 |
|      | <td>0.000099</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adfm.201801484">https://doi.org/10.1002/adfm.201801484</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2S4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.53</td>                                                |
|      | <td>0.000041</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122337">https://doi.org/10.1016/j.talanta.2021.122337</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2S4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.664</td>                                               |
|      | <td>0.000015</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122337">https://doi.org/10.1016/j.talanta.2021.122337</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtRu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.76</td>                                                |
|      | <td>0.0075</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.colsurfb.2021.111783">https://doi.org/10.1016/j.colsurfb.2021.111783</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtRu</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>36</td>                                                  |
|      | <td>0.00374</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.colsurfb.2021.111783">https://doi.org/10.1016/j.colsurfb.2021.111783</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoNiS3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.821</td>                                               |
|      | <td>0.006821</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8NJ04647F">https://doi.org/10.1039/C8NJ04647F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoNiS3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>1.247</td>                                               |
|      | <td>0.000692</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8NJ04647F">https://doi.org/10.1039/C8NJ04647F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0114</td>                                              |
|      | <td>0.000482</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.08.062">https://doi.org/10.1016/j.bios.2014.08.062</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>39.1</td>                                                |
|      | <td>0.0000138</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.08.062">https://doi.org/10.1016/j.bios.2014.08.062</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0067</td>                                              |
|      | <td>0.00000267</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.08.062">https://doi.org/10.1016/j.bios.2014.08.062</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>208</td>                                                 |
|      | <td>0.0000132</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.08.062">https://doi.org/10.1016/j.bios.2014.08.062</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0212</td>                                              |
|      | <td>0.00002814</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.07.168">https://doi.org/10.1016/j.snb.2016.07.168</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>2.27</td>                                                |
|      | <td>0.00000971</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2016.07.168">https://doi.org/10.1016/j.snb.2016.07.168</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.9Cu0.1</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.213</td>                                               |
|      | <td>0.00087</td>                                             |
|      | <td><a href="https://doi.org/10.1007/s00604-019-3293-0">https://doi.org/10.1007/s00604-019-3293-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.9Cu0.1</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.191</td>                                               |
|      | <td>0.0000664</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-019-3293-0">https://doi.org/10.1007/s00604-019-3293-0</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.5Ni0.5Co2O4</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0014</td>                                              |
|      | <td>0.001044</td>                                            |
|      | <td><a href="https://doi.org/10.1002/ejic.202200387">https://doi.org/10.1002/ejic.202200387</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.5Ni0.5Co2O4</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0029</td>                                              |
|      | <td>0.0003471</td>                                           |
|      | <td><a href="https://doi.org/10.1002/ejic.202200387">https://doi.org/10.1002/ejic.202200387</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.62</td>                                                |
|      | <td>0.0001664</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2019.111450">https://doi.org/10.1016/j.bios.2019.111450</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuS</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.94</td>                                                |
|      | <td>0.0000255</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2019.111450">https://doi.org/10.1016/j.bios.2019.111450</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.097</td>                                               |
|      | <td>0.0000746</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.08.078">https://doi.org/10.1016/j.bios.2014.08.078</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>199.4</td>                                               |
|      | <td>0.0000934</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2014.08.078">https://doi.org/10.1016/j.bios.2014.08.078</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt3Ni </td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.31</td>                                                |
|      | <td>0.0002812</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2019.111756">https://doi.org/10.1016/j.bios.2019.111756</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt3Ni </td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>1.2</td>                                                 |
|      | <td>0.0019608</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2019.111756">https://doi.org/10.1016/j.bios.2019.111756</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.2-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.016</td>                                               |
|      | <td>0.00002008</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.bios.2021.113724">https://doi.org/10.1016/j.bios.2021.113724</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.2-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>112.35</td>                                              |
|      | <td>0.0003871</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2021.113724">https://doi.org/10.1016/j.bios.2021.113724</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.2-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.017</td>                                               |
|      | <td>0.0002515</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2021.113724">https://doi.org/10.1016/j.bios.2021.113724</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.2-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>126.73</td>                                              |
|      | <td>0.0006667</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2021.113724">https://doi.org/10.1016/j.bios.2021.113724</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.2-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.031</td>                                               |
|      | <td>0.0006821</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2021.113724">https://doi.org/10.1016/j.bios.2021.113724</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.2-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>177.24</td>                                              |
|      | <td>0.0007463</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.bios.2021.113724">https://doi.org/10.1016/j.bios.2021.113724</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.0000114</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.inorgchem.9b03512">https://doi.org/10.1021/acs.inorgchem.9b03512</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3.43</td>                                                |
|      | <td>0.0000103</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.inorgchem.9b03512">https://doi.org/10.1021/acs.inorgchem.9b03512</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.07</td>                                                |
|      | <td>0.000158</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.inorgchem.9b03512">https://doi.org/10.1021/acs.inorgchem.9b03512</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.74</td>                                                |
|      | <td>0.0001013</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.inorgchem.9b03512">https://doi.org/10.1021/acs.inorgchem.9b03512</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.5</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>8.53</td>                                                |
|      | <td>0.000153</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>8.84</td>                                                |
|      | <td>0.00016</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>11.1</td>                                                |
|      | <td>0.000202</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>11.3</td>                                                |
|      | <td>0.0000217</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu0.45</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>13.5</td>                                                |
|      | <td>0.000236</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu0.65</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>16.3</td>                                                |
|      | <td>0.000292</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu0.7</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>19.6</td>                                                |
|      | <td>0.00035</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu0.8</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>20.2</td>                                                |
|      | <td>0.000362</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>20.7</td>                                                |
|      | <td>0.000354</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu1.2</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>19.9</td>                                                |
|      | <td>0.00036</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu1.3</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>20.5</td>                                                |
|      | <td>0.000371</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.3</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>5.55</td>                                                |
|      | <td>0.000162</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.35</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>6.54</td>                                                |
|      | <td>0.000215</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>6.46</td>                                                |
|      | <td>0.00021</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.45</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>5.97</td>                                                |
|      | <td>0.000203</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.6</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>6.03</td>                                                |
|      | <td>0.000155</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>67.1</td>                                                |
|      | <td>0.00006</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.82</td>                                                |
|      | <td>0.0000463</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>5.29</td>                                                |
|      | <td>0.000113</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>1.72</td>                                                |
|      | <td>0.0000265</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>1.23</td>                                                |
|      | <td>0.0000172</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>1.18</td>                                                |
|      | <td>0.0000565</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>1.79</td>                                                |
|      | <td>0.0000398</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>112</td>                                                 |
|      | <td>0.0043</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>223</td>                                                 |
|      | <td>0.00982</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>100</td>                                                 |
|      | <td>0.00304</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3</td>                                               |
|      | <td>catalase</td>                                            |
|      | <td>240</td>                                                 |
|      | <td>8</td>                                                   |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt3Cu</td>                                             |
|      | <td>catalase</td>                                            |
|      | <td>110</td>                                                 |
|      | <td>6</td>                                                   |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PtCu0.4</td>                                             |
|      | <td>catalase</td>                                            |
|      | <td>90</td>                                                  |
|      | <td>2</td>                                                   |
|      | <td><a href="https://doi.org/10.1016/j.cej.2023.142494">https://doi.org/10.1016/j.cej.2023.142494</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdIr0.5</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.22</td>                                                |
|      | <td>0.000071</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsanm.2c05400">https://doi.org/10.1021/acsanm.2c05400</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdIr0.5</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>11.41</td>                                               |
|      | <td>0.00011</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsanm.2c05400">https://doi.org/10.1021/acsanm.2c05400</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdRh0.03Ir0.03</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.000083</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsanm.2c05400">https://doi.org/10.1021/acsanm.2c05400</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdRh0.03Ir0.03</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>7.73</td>                                                |
|      | <td>0.00014</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsanm.2c05400">https://doi.org/10.1021/acsanm.2c05400</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.48Pd0.52-Fe3O4</td>                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.079</td>                                               |
|      | <td>0.0000936</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adma.201203218">https://doi.org/10.1002/adma.201203218</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.48Pd0.52-Fe3O4</td>                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.171</td>                                               |
|      | <td>0.0000444</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adma.201203218">https://doi.org/10.1002/adma.201203218</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt0.48Pd0.52</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.047</td>                                               |
|      | <td>0.0000256</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adma.201203218">https://doi.org/10.1002/adma.201203218</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.139</td>                                               |
|      | <td>0.0000346</td>                                           |
|      | <td><a href="https://doi.org/10.1002/adma.201203218">https://doi.org/10.1002/adma.201203218</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>172.41</td>                                              |
|      | <td>0.00000049</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>270.27</td>                                              |
|      | <td>0.000000375</td>                                         |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>catalase</td>                                            |
|      | <td>555.56</td>                                              |
|      | <td>0.000000307</td>                                         |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>catalase</td>                                            |
|      | <td>185.18</td>                                              |
|      | <td>0.000000203</td>                                         |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>156.25</td>                                              |
|      | <td>0.000000385</td>                                         |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>186.22</td>                                              |
|      | <td>0.000000307</td>                                         |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>36.71</td>                                               |
|      | <td>0.00002222</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>40.48</td>                                               |
|      | <td>0.0000184</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>3.9</td>                                                 |
|      | <td>0.0001128</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>VO2</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>4.38</td>                                                |
|      | <td>0.0000664</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>39.2</td>                                                |
|      | <td>0.0000136</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.2c20878">https://doi.org/10.1021/acsami.2c20878</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt </td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.24</td>                                                |
|      | <td>0.00082</td>                                             |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt </td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>3400</td>                                                |
|      | <td>0.001</td>                                               |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt3-Ru</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.35</td>                                                |
|      | <td>0.00096</td>                                             |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt3-Ru</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>1400</td>                                                |
|      | <td>0.0025</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.45</td>                                                |
|      | <td>0.0031</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>580</td>                                                 |
|      | <td>0.002</td>                                               |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru3</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.63</td>                                                |
|      | <td>0.002</td>                                               |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru3</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>320</td>                                                 |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.825Pt0.094Ru0.081</td>                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.42</td>                                                |
|      | <td>0.0012</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.825Pt0.094Ru0.081</td>                               |
|      | <td>peroxidase</td>                                          |
|      | <td>400</td>                                                 |
|      | <td>0.00089</td>                                             |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.825Pt0.094Ru0.081</td>                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.49</td>                                                |
|      | <td>0.002</td>                                               |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd0.825Pt0.094Ru0.081</td>                               |
|      | <td>peroxidase</td>                                          |
|      | <td>430</td>                                                 |
|      | <td>0.0014</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.8</td>                                                 |
|      | <td>0.0018</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>240</td>                                                 |
|      | <td>0.00068</td>                                             |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.63</td>                                                |
|      | <td>0.002</td>                                               |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt-Ru</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>320</td>                                                 |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D2NR01375D">https://doi.org/10.1039/D2NR01375D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag0.26-Au0.3@CeO2</td>                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>8.5</td>                                                 |
|      | <td>0.0000019</td>                                           |
|      | <td><a href="https://doi.org/10.1002/smll.201903182">https://doi.org/10.1002/smll.201903182</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag0.26-Au0.3@CeO2</td>                                   |
|      | <td>oxidase</td>                                             |
|      | <td>3</td>                                                   |
|      | <td>0.0001</td>                                              |
|      | <td><a href="https://doi.org/10.1002/smll.201903182">https://doi.org/10.1002/smll.201903182</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.663</td>                                               |
|      | <td>0.000221</td>                                            |
|      | <td><a href="https://doi.org/10.3390/chemosensors10090359">https://doi.org/10.3390/chemosensors10090359</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>3820</td>                                                |
|      | <td>0.000186</td>                                            |
|      | <td><a href="https://doi.org/10.3390/chemosensors10090359">https://doi.org/10.3390/chemosensors10090359</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>1.831</td>                                               |
|      | <td>0.00001097</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2021.06.170">https://doi.org/10.1016/j.jcis.2021.06.170</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>3.133</td>                                               |
|      | <td>0.00001011</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2021.06.170">https://doi.org/10.1016/j.jcis.2021.06.170</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.158</td>                                               |
|      | <td>0.0003843</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2021.06.170">https://doi.org/10.1016/j.jcis.2021.06.170</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>6.794</td>                                               |
|      | <td>0.0013262</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2021.06.170">https://doi.org/10.1016/j.jcis.2021.06.170</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.48</td>                                                |
|      | <td>0.00071</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.sintl.2020.100031">https://doi.org/10.1016/j.sintl.2020.100031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>390</td>                                                 |
|      | <td>0.00042</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.sintl.2020.100031">https://doi.org/10.1016/j.sintl.2020.100031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.34</td>                                                |
|      | <td>0.0006</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.sintl.2020.100031">https://doi.org/10.1016/j.sintl.2020.100031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>770</td>                                                 |
|      | <td>0.00058</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.sintl.2020.100031">https://doi.org/10.1016/j.sintl.2020.100031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.45</td>                                                |
|      | <td>0.00032</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.sintl.2020.100031">https://doi.org/10.1016/j.sintl.2020.100031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>350</td>                                                 |
|      | <td>0.00026</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.sintl.2020.100031">https://doi.org/10.1016/j.sintl.2020.100031</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.12</td>                                                |
|      | <td>0.00126</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.aca.2013.03.034">https://doi.org/10.1016/j.aca.2013.03.034</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>769</td>                                                 |
|      | <td>0.00185</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.aca.2013.03.034">https://doi.org/10.1016/j.aca.2013.03.034</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>1.66</td>                                                |
|      | <td>0.0000397</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129560">https://doi.org/10.1016/j.snb.2021.129560</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>13.2</td>                                                |
|      | <td>0.0000135</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129560">https://doi.org/10.1016/j.snb.2021.129560</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.1/Co3O4-CeO2</td>                                    |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1219</td>                                              |
|      | <td>0.000008577</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.05.108">https://doi.org/10.1016/j.snb.2018.05.108</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.1/Co3O4-CeO2</td>                                    |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2724</td>                                              |
|      | <td>0.000003898</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.05.108">https://doi.org/10.1016/j.snb.2018.05.108</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMoO4</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>0.0428</td>                                              |
|      | <td>0.0000872</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.microc.2023.108562">https://doi.org/10.1016/j.microc.2023.108562</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3V2O8</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.536</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.jiec.2021.09.034">https://doi.org/10.1016/j.jiec.2021.09.034</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3V2O8</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>4.8</td>                                                 |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.jiec.2021.09.034">https://doi.org/10.1016/j.jiec.2021.09.034</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3V2O8</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.27</td>                                                |
|      | <td>0.000101</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jiec.2021.09.034">https://doi.org/10.1016/j.jiec.2021.09.034</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/CuO</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.222</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1016/j.msec.2018.10.038">https://doi.org/10.1016/j.msec.2018.10.038</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(Co,Mn)3O4</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.0072</td>                                              |
|      | <td>0.0002086</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.aca.2022.339564">https://doi.org/10.1016/j.aca.2022.339564</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.02/Fe2O3</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0429</td>                                              |
|      | <td>0.05882</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.7b02880">https://doi.org/10.1021/acs.analchem.7b02880</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au0.02/Fe2O3</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>138.5</td>                                               |
|      | <td>0.0477</td>                                              |
|      | <td><a href="https://doi.org/10.1021/acs.analchem.7b02880">https://doi.org/10.1021/acs.analchem.7b02880</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt/ZnCo2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1357</td>                                              |
|      | <td>0.0008068</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0NJ02795B">https://doi.org/10.1039/D0NJ02795B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt/ZnCo2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.73</td>                                                |
|      | <td>0.0000835</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0NJ02795B">https://doi.org/10.1039/D0NJ02795B</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0398</td>                                              |
|      | <td>0.0045</td>                                              |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2020.125397">https://doi.org/10.1016/j.colsurfa.2020.125397</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0158</td>                                              |
|      | <td>0.0004167</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2020.125397">https://doi.org/10.1016/j.colsurfa.2020.125397</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaMnO3.15</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.037</td>                                               |
|      | <td>0.0000768</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C8TB01706A">https://doi.org/10.1039/C8TB01706A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V6O13</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.153</td>                                               |
|      | <td>0.0000299</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.iecr.7b04821">https://doi.org/10.1021/acs.iecr.7b04821</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V6O13</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.51</td>                                                |
|      | <td>0.0000312</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acs.iecr.7b04821">https://doi.org/10.1021/acs.iecr.7b04821</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnCo2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.063</td>                                               |
|      | <td>0.0217</td>                                              |
|      | <td><a href="https://doi.org/10.1021/acsanm.8b00895">https://doi.org/10.1021/acsanm.8b00895</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt/CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.408</td>                                               |
|      | <td>0.000884</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2019.02.135">https://doi.org/10.1016/j.apsusc.2019.02.135</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt/CeO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>16.18</td>                                               |
|      | <td>0.001082</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2019.02.135">https://doi.org/10.1016/j.apsusc.2019.02.135</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMn2O4/Mn2O3</td>                                       |
|      | <td>oxidase</td>                                             |
|      | <td>0.0378</td>                                              |
|      | <td>0.000044</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.126928">https://doi.org/10.1016/j.snb.2019.126928</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn2O3</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.0856</td>                                              |
|      | <td>0.0000286</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.126928">https://doi.org/10.1016/j.snb.2019.126928</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>2.01</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b05036">https://doi.org/10.1021/acsami.7b05036</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pr0.05-CeO2</td>                                         |
|      | <td>oxidase</td>                                             |
|      | <td>0.79</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b05036">https://doi.org/10.1021/acsami.7b05036</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pr0.1-CeO2</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.27</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b05036">https://doi.org/10.1021/acsami.7b05036</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pr0.15-CeO2</td>                                         |
|      | <td>oxidase</td>                                             |
|      | <td>0.23</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b05036">https://doi.org/10.1021/acsami.7b05036</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pr0.2-CeO2</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>0.15</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.7b05036">https://doi.org/10.1021/acsami.7b05036</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn0.6Co0.4O</td>                                         |
|      | <td>oxidase</td>                                             |
|      | <td>0.0187</td>                                              |
|      | <td>0.0000762</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0CC06209J">https://doi.org/10.1039/D0CC06209J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3/Fe4(Fe(CN)6)4</td>                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>0.01</td>                                                |
|      | <td>0.000123</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.molcata.2012.04.011">https://doi.org/10.1016/j.molcata.2012.04.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3/Fe4(Fe(CN)6)4</td>                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>15</td>                                                  |
|      | <td>0.000228</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.molcata.2012.04.011">https://doi.org/10.1016/j.molcata.2012.04.011</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni/CoMoO4</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.076</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsnano.1c11012">https://doi.org/10.1021/acsnano.1c11012</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni/CoMoO4</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.008</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsnano.1c11012">https://doi.org/10.1021/acsnano.1c11012</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni/CoMoO4</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.09</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsnano.1c11012">https://doi.org/10.1021/acsnano.1c11012</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.214</td>                                               |
|      | <td>0.0000212</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>115</td>                                                 |
|      | <td>0.0000289</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.45</td>                                                |
|      | <td>0.00000961</td>                                          |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0571</td>                                              |
|      | <td>0.0000908</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>236</td>                                                 |
|      | <td>0.000166</td>                                            |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>581</td>                                                 |
|      | <td>0.0000392</td>                                           |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>452</td>                                                 |
|      | <td>0.000392</td>                                            |
|      | <td><a href="https://doi.org/10.1088/1361-6528/aaddc2">https://doi.org/10.1088/1361-6528/aaddc2</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.0001</td>                                              |
|      | <td>38780</td>                                               |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.123939">https://doi.org/10.1016/j.jhazmat.2020.123939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4-Au0.44</td>                                      |
|      | <td>oxidase</td>                                             |
|      | <td>0.0001</td>                                              |
|      | <td>34537</td>                                               |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.123939">https://doi.org/10.1016/j.jhazmat.2020.123939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0002</td>                                              |
|      | <td>59885</td>                                               |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.123939">https://doi.org/10.1016/j.jhazmat.2020.123939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0283</td>                                              |
|      | <td>28773</td>                                               |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.123939">https://doi.org/10.1016/j.jhazmat.2020.123939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4-Au0.44</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0002</td>                                              |
|      | <td>56163</td>                                               |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.123939">https://doi.org/10.1016/j.jhazmat.2020.123939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2O4-Au0.44</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0132</td>                                              |
|      | <td>29250</td>                                               |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.123939">https://doi.org/10.1016/j.jhazmat.2020.123939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co(OH)2</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.362</td>                                               |
|      | <td>0.0000606</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.aca.2020.07.068">https://doi.org/10.1016/j.aca.2020.07.068</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BNCuS</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.175</td>                                               |
|      | <td>0.0000376</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.02.059">https://doi.org/10.1016/j.snb.2017.02.059</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>BNCuS</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>25</td>                                                  |
|      | <td>0.000125</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2017.02.059">https://doi.org/10.1016/j.snb.2017.02.059</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>27.09</td>                                               |
|      | <td>0.0001373</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2022.132066">https://doi.org/10.1016/j.snb.2022.132066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>21.54</td>                                               |
|      | <td>0.0004507</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2022.132066">https://doi.org/10.1016/j.snb.2022.132066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>16.54</td>                                               |
|      | <td>0.0008745</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2022.132066">https://doi.org/10.1016/j.snb.2022.132066</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.25</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.026</td>                                               |
|      | <td>0.000096</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.17</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0056</td>                                              |
|      | <td>0.000032</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.10</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0021</td>                                              |
|      | <td>0.000016</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.25</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.026</td>                                               |
|      | <td>0.0000312</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.25</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.163</td>                                               |
|      | <td>0.0001212</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.25</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.251</td>                                               |
|      | <td>0.0000036</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au-Pt0.25</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.184</td>                                               |
|      | <td>0.0000171</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.03.045">https://doi.org/10.1016/j.snb.2012.03.045</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiMoO4-Cu</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.541</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.0c03822">https://doi.org/10.1021/acssuschemeng.0c03822</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiMoO4-Cu</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>9.042</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.0c03822">https://doi.org/10.1021/acssuschemeng.0c03822</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMoO4-Cu</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>0.365</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.0c03822">https://doi.org/10.1021/acssuschemeng.0c03822</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMoO4-Cu</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>1.772</td>                                               |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.0c03822">https://doi.org/10.1021/acssuschemeng.0c03822</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NHMoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>5.06</td>                                                |
|      | <td>0.00166</td>                                             |
|      | <td><a href="https://doi.org/10.1002/ange.202115939">https://doi.org/10.1002/ange.202115939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NHMoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>2.41</td>                                                |
|      | <td>0.00013</td>                                             |
|      | <td><a href="https://doi.org/10.1002/ange.202115939">https://doi.org/10.1002/ange.202115939</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt </td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.09</td>                                                |
|      | <td>0.0000427</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.1c10600">https://doi.org/10.1021/acsami.1c10600</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.000152</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6AN02722A">https://doi.org/10.1039/C6AN02722A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.000129</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6AN02722A">https://doi.org/10.1039/C6AN02722A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.0000563</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6AN02722A">https://doi.org/10.1039/C6AN02722A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.0000473</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6AN02722A">https://doi.org/10.1039/C6AN02722A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.48</td>                                                |
|      | <td>0.00079</td>                                             |
|      | <td><a href="https://doi.org/10.1021/jacs.0c12605">https://doi.org/10.1021/jacs.0c12605</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni@Pt2</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>9</td>                                                   |
|      | <td>0.0061</td>                                              |
|      | <td><a href="https://doi.org/10.1021/jacs.0c12605">https://doi.org/10.1021/jacs.0c12605</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>35</td>                                                  |
|      | <td>0.026</td>                                               |
|      | <td><a href="https://doi.org/10.1021/jacs.0c12605">https://doi.org/10.1021/jacs.0c12605</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ni@Pt0.5</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>13</td>                                                  |
|      | <td>0.15</td>                                                |
|      | <td><a href="https://doi.org/10.1021/jacs.0c12605">https://doi.org/10.1021/jacs.0c12605</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SrFeO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>6.05</td>                                                |
|      | <td>0.00018</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>La0.5Sr0.5MnO3</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>40.08</td>                                               |
|      | <td>0.00054</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>La0.5Sr0.5FeO3</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>8.14</td>                                                |
|      | <td>0.00013</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaNiO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>359.92</td>                                              |
|      | <td>0.00463</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaNiO3-H2</td>                                           |
|      | <td>peroxidase</td>                                          |
|      | <td>125.96</td>                                              |
|      | <td>0.00145</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaMnO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>31.46</td>                                               |
|      | <td>0.00068</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaMn0.5Ni0.5O3</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>112.84</td>                                              |
|      | <td>0.00044</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>92.1</td>                                                |
|      | <td>0.00114</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaCoO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>205.45</td>                                              |
|      | <td>0.00093</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>4.41</td>                                                |
|      | <td>0.00018</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>75.97</td>                                               |
|      | <td>0.000068</td>                                            |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>41.66</td>                                               |
|      | <td>0.00016</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO </td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>31.18</td>                                               |
|      | <td>0.00028</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>41.75</td>                                               |
|      | <td>0.00026</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>12.53</td>                                               |
|      | <td>0.00101</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu(OH)2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>28.91</td>                                               |
|      | <td>0.00034</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaCrO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.00017</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>LaFeO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.00019</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CaMnO3</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.00015</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiO</td>                                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.00011</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.0000064</td>                                           |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Mn3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>no</td>                                                  |
|      | <td>0.00013</td>                                             |
|      | <td><a href="https://doi.org/10.1038/s41467-019-08657-5">https://doi.org/10.1038/s41467-019-08657-5</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu(OH)2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>2.448</td>                                               |
|      | <td>0.0004483</td>                                           |
|      | <td><a href="https://doi.org/10.1021/jacs.5b09337">https://doi.org/10.1021/jacs.5b09337</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu(OH)2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.199</td>                                               |
|      | <td>0.0004251</td>                                           |
|      | <td><a href="https://doi.org/10.1021/jacs.5b09337">https://doi.org/10.1021/jacs.5b09337</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.153</td>                                               |
|      | <td>0.0000294</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b13835">https://doi.org/10.1021/acsami.7b13835</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>86.425</td>                                              |
|      | <td>0.0000305</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b13835">https://doi.org/10.1021/acsami.7b13835</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.214</td>                                               |
|      | <td>0.0000274</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b13835">https://doi.org/10.1021/acsami.7b13835</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>125.904</td>                                             |
|      | <td>0.0000289</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b13835">https://doi.org/10.1021/acsami.7b13835</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.236</td>                                               |
|      | <td>0.0000265</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b13835">https://doi.org/10.1021/acsami.7b13835</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>132.9175</td>                                            |
|      | <td>0.0000289</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.7b13835">https://doi.org/10.1021/acsami.7b13835</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.28</td>                                                |
|      | <td>0.00465</td>                                             |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>3.425</td>                                               |
|      | <td>0.007783333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.671</td>                                               |
|      | <td>0.0072</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.958</td>                                               |
|      | <td>0.010033333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0444</td>                                              |
|      | <td>0.00321</td>                                             |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0573</td>                                              |
|      | <td>0.003883333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0925</td>                                              |
|      | <td>0.005666667</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2O5</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.143</td>                                               |
|      | <td>0.002383333</td>                                         |
|      | <td><a href="https://doi.org/10.1002/anie.201800681">https://doi.org/10.1002/anie.201800681</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4/Rh0.125</td>                                       |
|      | <td>oxidase</td>                                             |
|      | <td>0.018</td>                                               |
|      | <td>0.0000645</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jhazmat.2020.125019">https://doi.org/10.1016/j.jhazmat.2020.125019</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0003</td>                                              |
|      | <td>2.7</td>                                                 |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2023.157185">https://doi.org/10.1016/j.apsusc.2023.157185</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.281</td>                                               |
|      | <td>85.9</td>                                                |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2023.157185">https://doi.org/10.1016/j.apsusc.2023.157185</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(Fe3O4)0.1/CuO1.5</td>                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0012</td>                                              |
|      | <td>25.1</td>                                                |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2023.157185">https://doi.org/10.1016/j.apsusc.2023.157185</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(Fe3O4)0.1/CuO1.5</td>                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.03</td>                                                |
|      | <td>12.3</td>                                                |
|      | <td><a href="https://doi.org/10.1016/j.apsusc.2023.157185">https://doi.org/10.1016/j.apsusc.2023.157185</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.81</td>                                                |
|      | <td>0.000276</td>                                            |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.66</td>                                                |
|      | <td>0.000386</td>                                            |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.71</td>                                                |
|      | <td>0.000512</td>                                            |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.73</td>                                                |
|      | <td>0.00033</td>                                             |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.42</td>                                                |
|      | <td>0.00011</td>                                             |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.52</td>                                                |
|      | <td>0.00024</td>                                             |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.81</td>                                                |
|      | <td>0.0003</td>                                              |
|      | <td><a href="https://doi.org/10.1002/cnma.201600268">https://doi.org/10.1002/cnma.201600268</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1646</td>                                              |
|      | <td>0.0006354</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0NJ05026A">https://doi.org/10.1039/D0NJ05026A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuCo2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.59</td>                                                |
|      | <td>0.0000683</td>                                           |
|      | <td><a href="https://doi.org/10.1039/D0NJ05026A">https://doi.org/10.1039/D0NJ05026A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.51</td>                                                |
|      | <td>0.0000103</td>                                           |
|      | <td><a href="https://doi.org/10.3390/nano9020210">https://doi.org/10.3390/nano9020210</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>5.3</td>                                                 |
|      | <td>0.0000096</td>                                           |
|      | <td><a href="https://doi.org/10.3390/nano9020210">https://doi.org/10.3390/nano9020210</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.3</td>                                                 |
|      | <td>0.000098</td>                                            |
|      | <td><a href="https://doi.org/10.1021/cm8031863">https://doi.org/10.1021/cm8031863</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.5</td>                                                 |
|      | <td>0.000116</td>                                            |
|      | <td><a href="https://doi.org/10.1021/cm8031863">https://doi.org/10.1021/cm8031863</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru0.85Cu0.15</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.299</td>                                               |
|      | <td>0.000556</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adhm.202300490">https://doi.org/10.1002/adhm.202300490</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru0.85Cu0.15</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.28</td>                                                |
|      | <td>0.000476</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adhm.202300490">https://doi.org/10.1002/adhm.202300490</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ru0.85Cu0.15</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.408</td>                                               |
|      | <td>0.000357</td>                                            |
|      | <td><a href="https://doi.org/10.1002/adhm.202300490">https://doi.org/10.1002/adhm.202300490</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.198</td>                                               |
|      | <td>0.0000678</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2582-8">https://doi.org/10.1007/s00604-017-2582-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Rh</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.38</td>                                                |
|      | <td>0.000241</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2582-8">https://doi.org/10.1007/s00604-017-2582-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1098</td>                                              |
|      | <td>0.0000582</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5NR05675F">https://doi.org/10.1039/C5NR05675F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>4.398</td>                                               |
|      | <td>0.0000651</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5NR05675F">https://doi.org/10.1039/C5NR05675F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0865</td>                                              |
|      | <td>0.00006228</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C5NR05675F">https://doi.org/10.1039/C5NR05675F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Pt</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>2.231</td>                                               |
|      | <td>0.00005</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C5NR05675F">https://doi.org/10.1039/C5NR05675F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0022</td>                                              |
|      | <td>0.000017495</td>                                         |
|      | <td><a href="https://doi.org/10.1039/C7NJ03880A">https://doi.org/10.1039/C7NJ03880A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>20.492</td>                                              |
|      | <td>0.0003423</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C7NJ03880A">https://doi.org/10.1039/C7NJ03880A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(CeO2)0.10/Co3O4</td>                                    |
|      | <td>peroxidase</td>                                          |
|      | <td>0.14</td>                                                |
|      | <td>0.000413</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6TB02750D">https://doi.org/10.1039/C6TB02750D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(CeO2)0.10/Co3O4</td>                                    |
|      | <td>peroxidase</td>                                          |
|      | <td>7.09</td>                                                |
|      | <td>0.000433</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C6TB02750D">https://doi.org/10.1039/C6TB02750D</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2(OH)3Cl-CeO2</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>12.36</td>                                               |
|      | <td>0.0001062</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1506-8">https://doi.org/10.1007/s00604-015-1506-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu2(OH)3Cl-CeO2</td>                                     |
|      | <td>peroxidase</td>                                          |
|      | <td>11.61</td>                                               |
|      | <td>0.0000815</td>                                           |
|      | <td><a href="https://doi.org/10.1007/s00604-015-1506-8">https://doi.org/10.1007/s00604-015-1506-8</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.173</td>                                               |
|      | <td>0.000172</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2198-z">https://doi.org/10.1007/s00604-017-2198-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>185</td>                                                 |
|      | <td>0.282</td>                                               |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2198-z">https://doi.org/10.1007/s00604-017-2198-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.187</td>                                               |
|      | <td>0.000591</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2198-z">https://doi.org/10.1007/s00604-017-2198-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>30</td>                                                  |
|      | <td>0.58</td>                                                |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2198-z">https://doi.org/10.1007/s00604-017-2198-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.185</td>                                               |
|      | <td>0.000519</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2198-z">https://doi.org/10.1007/s00604-017-2198-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>39</td>                                                  |
|      | <td>0.529</td>                                               |
|      | <td><a href="https://doi.org/10.1007/s00604-017-2198-z">https://doi.org/10.1007/s00604-017-2198-z</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuTe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>208.85</td>                                              |
|      | <td>0.0000266</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsnano.9b09974">https://doi.org/10.1021/acsnano.9b09974</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RuTe</td>                                                |
|      | <td>catalase</td>                                            |
|      | <td>0.0188</td>                                              |
|      | <td>0.0589</td>                                              |
|      | <td><a href="https://doi.org/10.1021/acsnano.9b09974">https://doi.org/10.1021/acsnano.9b09974</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.2Te</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.29</td>                                                |
|      | <td>0.0149</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.201909729">https://doi.org/10.1002/anie.201909729</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.2Te</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.19</td>                                                |
|      | <td>0.0193</td>                                              |
|      | <td><a href="https://doi.org/10.1002/anie.201909729">https://doi.org/10.1002/anie.201909729</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.2Te</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>189</td>                                                 |
|      | <td>0.00073</td>                                             |
|      | <td><a href="https://doi.org/10.1002/anie.201909729">https://doi.org/10.1002/anie.201909729</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu1.2Te</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>135</td>                                                 |
|      | <td>0.00087</td>                                             |
|      | <td><a href="https://doi.org/10.1002/anie.201909729">https://doi.org/10.1002/anie.201909729</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.1</td>                                                 |
|      | <td>0.0002</td>                                              |
|      | <td><a href="https://doi.org/10.1039/D3NJ00136A">https://doi.org/10.1039/D3NJ00136A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuMnO2</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>0.0499</td>                                              |
|      | <td>0.0007504</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.colsurfa.2022.129887">https://doi.org/10.1016/j.colsurfa.2022.129887</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO </td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.58</td>                                                |
|      | <td>0.0002014</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.1c00723">https://doi.org/10.1021/acssuschemeng.1c00723</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CuO </td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.09</td>                                                |
|      | <td>0.0000468</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.1c00723">https://doi.org/10.1021/acssuschemeng.1c00723</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RhPt</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.129</td>                                               |
|      | <td>0.0006815</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsanm.1c01457">https://doi.org/10.1021/acsanm.1c01457</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>RhPt</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>6.18</td>                                                |
|      | <td>0.000927</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsanm.1c01457">https://doi.org/10.1021/acsanm.1c01457</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1206</td>                                              |
|      | <td>0.0000651</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac503544w">https://doi.org/10.1021/ac503544w</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>205.6</td>                                               |
|      | <td>0.0000979</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac503544w">https://doi.org/10.1021/ac503544w</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Hg0.01Pt</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1337</td>                                              |
|      | <td>0.0000385</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac503544w">https://doi.org/10.1021/ac503544w</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Hg0.01Pt</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>221.9</td>                                               |
|      | <td>0.0000269</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac503544w">https://doi.org/10.1021/ac503544w</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Hg0.1Pt</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.257</td>                                               |
|      | <td>0.0000372</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac503544w">https://doi.org/10.1021/ac503544w</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Hg0.1Pt</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>295</td>                                                 |
|      | <td>0.0000223</td>                                           |
|      | <td><a href="https://doi.org/10.1021/ac503544w">https://doi.org/10.1021/ac503544w</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag3PO4</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>3.31</td>                                                |
|      | <td>0.00277</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C5DT04192A">https://doi.org/10.1039/C5DT04192A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag3PO4</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>2.09</td>                                                |
|      | <td>0.0242</td>                                              |
|      | <td><a href="https://doi.org/10.1039/C5DT04192A">https://doi.org/10.1039/C5DT04192A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag/Ag3PO4</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>1.23</td>                                                |
|      | <td>0.00518</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C5DT04192A">https://doi.org/10.1039/C5DT04192A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ag/Ag3PO4</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.11</td>                                                |
|      | <td>0.00632</td>                                             |
|      | <td><a href="https://doi.org/10.1039/C5DT04192A">https://doi.org/10.1039/C5DT04192A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(CeO2)0.1/TiO2</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.097</td>                                               |
|      | <td>0.0000554</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.5b00023">https://doi.org/10.1021/acsami.5b00023</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>(CeO2)0.1/TiO2</td>                                      |
|      | <td>peroxidase</td>                                          |
|      | <td>0.04</td>                                                |
|      | <td>0.0000227</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.5b00023">https://doi.org/10.1021/acsami.5b00023</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.15-CoO</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.17</td>                                                |
|      | <td>0.000509</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.inorgchem.0c03355">https://doi.org/10.1021/acs.inorgchem.0c03355</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe0.15-CoO</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>11.2</td>                                                |
|      | <td>0.000241</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.inorgchem.0c03355">https://doi.org/10.1021/acs.inorgchem.0c03355</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>1.06</td>                                                |
|      | <td>0.000168</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8RA05487H">https://doi.org/10.1039/C8RA05487H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>56.89</td>                                               |
|      | <td>0.000596</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8RA05487H">https://doi.org/10.1039/C8RA05487H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co0.5-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>1.17</td>                                                |
|      | <td>0.000379</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8RA05487H">https://doi.org/10.1039/C8RA05487H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co0.5-Fe3O4</td>                                         |
|      | <td>peroxidase</td>                                          |
|      | <td>0.19</td>                                                |
|      | <td>0.000715</td>                                            |
|      | <td><a href="https://doi.org/10.1039/C8RA05487H">https://doi.org/10.1039/C8RA05487H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Cu-Cu2O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>0.85</td>                                                |
|      | <td>0.000131</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2016.04.269">https://doi.org/10.1016/j.jallcom.2016.04.269</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Cu-Cu2O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>2.3</td>                                                 |
|      | <td>0.000119</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2016.04.269">https://doi.org/10.1016/j.jallcom.2016.04.269</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Cu-Cu2O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>0.87</td>                                                |
|      | <td>0.000132</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2016.04.269">https://doi.org/10.1016/j.jallcom.2016.04.269</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Cu-Cu2O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>2.4</td>                                                 |
|      | <td>0.000125</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2016.04.269">https://doi.org/10.1016/j.jallcom.2016.04.269</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Cu-Cu2O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>0.155</td>                                               |
|      | <td>0.0000171</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2016.04.269">https://doi.org/10.1016/j.jallcom.2016.04.269</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4-Cu-Cu2O</td>                                       |
|      | <td>peroxidase</td>                                          |
|      | <td>116.3</td>                                               |
|      | <td>0.0000923</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2016.04.269">https://doi.org/10.1016/j.jallcom.2016.04.269</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3/Fe4(Fe(CN)6)4</td>                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>1.22</td>                                                |
|      | <td>0.00004431</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.11.074">https://doi.org/10.1016/j.snb.2012.11.074</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3/Fe4(Fe(CN)6)4</td>                                 |
|      | <td>peroxidase</td>                                          |
|      | <td>91.54</td>                                               |
|      | <td>0.00008308</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2012.11.074">https://doi.org/10.1016/j.snb.2012.11.074</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0265</td>                                              |
|      | <td>0.000000171</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.msec.2015.05.028">https://doi.org/10.1016/j.msec.2015.05.028</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0132</td>                                              |
|      | <td>0.000000434</td>                                         |
|      | <td><a href="https://doi.org/10.1016/j.msec.2015.05.028">https://doi.org/10.1016/j.msec.2015.05.028</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0887</td>                                              |
|      | <td>0.0000097</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C6RA00963H">https://doi.org/10.1039/C6RA00963H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>157.19</td>                                              |
|      | <td>0.00001284</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C6RA00963H">https://doi.org/10.1039/C6RA00963H</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Fe2O3</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.049</td>                                               |
|      | <td>0.000102</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.chemmater.6b04283">https://doi.org/10.1021/acs.chemmater.6b04283</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Fe2O3</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.254</td>                                               |
|      | <td>0.000128</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acs.chemmater.6b04283">https://doi.org/10.1021/acs.chemmater.6b04283</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd@Fe2O3</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.1</td>                                                 |
|      | <td>0.00017</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acs.chemmater.6b04283">https://doi.org/10.1021/acs.chemmater.6b04283</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Si-CoO</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0589</td>                                              |
|      | <td>0.00025</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.9b02459">https://doi.org/10.1021/acssuschemeng.9b02459</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Si-CoO</td>                                              |
|      | <td>peroxidase</td>                                          |
|      | <td>0.023</td>                                               |
|      | <td>0.000104</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.9b02459">https://doi.org/10.1021/acssuschemeng.9b02459</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiO2@Co3O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.087</td>                                               |
|      | <td>0.00000012</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4RA12596G">https://doi.org/10.1039/C4RA12596G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>SiO2@Co3O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>25.2</td>                                                |
|      | <td>0.00000015</td>                                          |
|      | <td><a href="https://doi.org/10.1039/C4RA12596G">https://doi.org/10.1039/C4RA12596G</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu-CuFe2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.39</td>                                                |
|      | <td>0.000239</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.surfin.2021.101109">https://doi.org/10.1016/j.surfin.2021.101109</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu-CuFe2O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.21</td>                                                |
|      | <td>0.000474</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.surfin.2021.101109">https://doi.org/10.1016/j.surfin.2021.101109</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3/CoNi</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.23</td>                                                |
|      | <td>0.000135</td>                                            |
|      | <td><a href="https://doi.org/10.1039/D1RA03456A">https://doi.org/10.1039/D1RA03456A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe2O3/CoNi</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.42</td>                                                |
|      | <td>0.000093</td>                                            |
|      | <td><a href="https://doi.org/10.1039/D1RA03456A">https://doi.org/10.1039/D1RA03456A</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2/Fe3O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>0.35</td>                                                |
|      | <td>0.00035</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.microc.2019.104019">https://doi.org/10.1016/j.microc.2019.104019</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2/Fe3O4</td>                                          |
|      | <td>peroxidase</td>                                          |
|      | <td>2.5</td>                                                 |
|      | <td>0.000033</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.microc.2019.104019">https://doi.org/10.1016/j.microc.2019.104019</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2@MgFe2O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.806</td>                                               |
|      | <td>0.001413</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.08.051">https://doi.org/10.1016/j.snb.2018.08.051</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2@MgFe2O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.238</td>                                               |
|      | <td>0.000378</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.08.051">https://doi.org/10.1016/j.snb.2018.08.051</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2@MgFe2O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>1.03</td>                                                |
|      | <td>0.000141</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2018.08.051">https://doi.org/10.1016/j.snb.2018.08.051</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2–Pt0.74Ag0.26</td>                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>25.71</td>                                               |
|      | <td>0.0000729</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5NR08038J">https://doi.org/10.1039/C5NR08038J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MoS2–Pt0.74Ag0.26</td>                                   |
|      | <td>peroxidase</td>                                          |
|      | <td>0.386</td>                                               |
|      | <td>0.0000322</td>                                           |
|      | <td><a href="https://doi.org/10.1039/C5NR08038J">https://doi.org/10.1039/C5NR08038J</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2S4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3</td>                                                 |
|      | <td>0.0003486</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2020.128850">https://doi.org/10.1016/j.snb.2020.128850</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>NiCo2S4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>4.5</td>                                                 |
|      | <td>0.0000432</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2020.128850">https://doi.org/10.1016/j.snb.2020.128850</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe-Ag2S</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0756</td>                                              |
|      | <td>0.0000209</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2019.01.225">https://doi.org/10.1016/j.jallcom.2019.01.225</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe-Ag2S</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.471</td>                                               |
|      | <td>0.000374</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jallcom.2019.01.225">https://doi.org/10.1016/j.jallcom.2019.01.225</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>4N-TiO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.45</td>                                                |
|      | <td>0.000115</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2017.07.014">https://doi.org/10.1016/j.jcis.2017.07.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>4N-TiO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.75</td>                                                |
|      | <td>0.000068</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2017.07.014">https://doi.org/10.1016/j.jcis.2017.07.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>4N-TiO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.35</td>                                                |
|      | <td>0.000071</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2017.07.014">https://doi.org/10.1016/j.jcis.2017.07.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>4N-TiO2</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.64</td>                                                |
|      | <td>0.000085</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.jcis.2017.07.014">https://doi.org/10.1016/j.jcis.2017.07.014</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdCu</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.127</td>                                               |
|      | <td>0.00008611</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.1c07568">https://doi.org/10.1021/acssuschemeng.1c07568</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.194</td>                                               |
|      | <td>0.00006246</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.1c07568">https://doi.org/10.1021/acssuschemeng.1c07568</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>PdCu</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.839</td>                                               |
|      | <td>0.00005254</td>                                          |
|      | <td><a href="https://doi.org/10.1021/acssuschemeng.1c07568">https://doi.org/10.1021/acssuschemeng.1c07568</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd/C</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.093</td>                                               |
|      | <td>0.0000179</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.9b16279">https://doi.org/10.1021/acsami.9b16279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd/C</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.117</td>                                               |
|      | <td>0.0000054</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.9b16279">https://doi.org/10.1021/acsami.9b16279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.101</td>                                               |
|      | <td>0.0000116</td>                                           |
|      | <td><a href="https://doi.org/10.1021/acsami.9b16279">https://doi.org/10.1021/acsami.9b16279</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd-As0.01</td>                                           |
|      | <td>oxidase</td>                                             |
|      | <td>0.17</td>                                                |
|      | <td>0.000028</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2019.126876">https://doi.org/10.1016/j.snb.2019.126876</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd3.5-Ir</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.27</td>                                                |
|      | <td>0.00063</td>                                             |
|      | <td><a href="https://doi.org/10.1002/cbic.202000147">https://doi.org/10.1002/cbic.202000147</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd3.5-Ir</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.64</td>                                                |
|      | <td>0.0013</td>                                              |
|      | <td><a href="https://doi.org/10.1002/cbic.202000147">https://doi.org/10.1002/cbic.202000147</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd3.5-Ir</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.4</td>                                                 |
|      | <td>0.00089</td>                                             |
|      | <td><a href="https://doi.org/10.1002/cbic.202000147">https://doi.org/10.1002/cbic.202000147</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd3.5-Ir</td>                                            |
|      | <td>peroxidase</td>                                          |
|      | <td>0.34</td>                                                |
|      | <td>0.00072</td>                                             |
|      | <td><a href="https://doi.org/10.1002/cbic.202000147">https://doi.org/10.1002/cbic.202000147</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.086</td>                                               |
|      | <td>0.0000152</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cclet.2021.08.017">https://doi.org/10.1016/j.cclet.2021.08.017</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd/C3N4</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.121</td>                                               |
|      | <td>0.0000105</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.cclet.2021.08.017">https://doi.org/10.1016/j.cclet.2021.08.017</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.0268</td>                                              |
|      | <td>0.00007084</td>                                          |
|      | <td><a href="https://doi.org/10.1021/jacs.0c09567">https://doi.org/10.1021/jacs.0c09567</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce2(CO3)2O</td>                                          |
|      | <td>oxidase</td>                                             |
|      | <td>2.33</td>                                                |
|      | <td>0.00001</td>                                             |
|      | <td><a href="https://doi.org/10.1021/acsanm.3c01652">https://doi.org/10.1021/acsanm.3c01652</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe–Mn</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.2</td>                                                 |
|      | <td>0.0001025</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.lwt.2021.112821">https://doi.org/10.1016/j.lwt.2021.112821</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.192</td>                                               |
|      | <td>0.0000816</td>                                           |
|      | <td><a href="https://doi.org/10.3390/nano12050755">https://doi.org/10.3390/nano12050755</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au@Pt</td>                                               |
|      | <td>oxidase</td>                                             |
|      | <td>0.268</td>                                               |
|      | <td>0.0000153</td>                                           |
|      | <td><a href="https://doi.org/10.3390/nano12050755">https://doi.org/10.3390/nano12050755</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2</td>                                                |
|      | <td>oxidase</td>                                             |
|      | <td>0.095</td>                                               |
|      | <td>0.00026</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.bios.2018.08.004">https://doi.org/10.1016/j.bios.2018.08.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.62</td>                                                |
|      | <td>0.000011</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.bios.2018.08.004">https://doi.org/10.1016/j.bios.2018.08.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt@MnO2</td>                                             |
|      | <td>oxidase</td>                                             |
|      | <td>0.015</td>                                               |
|      | <td>0.000156</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.bios.2018.08.004">https://doi.org/10.1016/j.bios.2018.08.004</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>MnO2/C</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>0.11</td>                                                |
|      | <td>0.000244</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsanm.2c03340">https://doi.org/10.1021/acsanm.2c03340</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu/Cu2O </td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.356</td>                                               |
|      | <td>0.64</td>                                                |
|      | <td><a href="https://doi.org/10.1038/s41467-021-23737-1">https://doi.org/10.1038/s41467-021-23737-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu/Cu2O </td>                                            |
|      | <td>oxidase</td>                                             |
|      | <td>0.189</td>                                               |
|      | <td>0.907</td>                                               |
|      | <td><a href="https://doi.org/10.1038/s41467-021-23737-1">https://doi.org/10.1038/s41467-021-23737-1</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Cu</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.7513</td>                                              |
|      | <td>0.00076</td>                                             |
|      | <td><a href="https://doi.org/10.1016/j.saa.2023.123003">https://doi.org/10.1016/j.saa.2023.123003</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.6819</td>                                              |
|      | <td>0.0001739</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122647">https://doi.org/10.1016/j.talanta.2021.122647</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.0092</td>                                              |
|      | <td>0.0001854</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122647">https://doi.org/10.1016/j.talanta.2021.122647</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.1369</td>                                              |
|      | <td>0.0001645</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2021.122647">https://doi.org/10.1016/j.talanta.2021.122647</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.201</td>                                               |
|      | <td>0.000777</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.carbpol.2022.120120">https://doi.org/10.1016/j.carbpol.2022.120120</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.385</td>                                               |
|      | <td>0.000528</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.carbpol.2022.120120">https://doi.org/10.1016/j.carbpol.2022.120120</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoMnO3</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>0.167</td>                                               |
|      | <td>0.000674</td>                                            |
|      | <td><a href="https://doi.org/10.1016/j.snb.2023.133540">https://doi.org/10.1016/j.snb.2023.133540</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>H-MnO2</td>                                              |
|      | <td>oxidase</td>                                             |
|      | <td>0.781</td>                                               |
|      | <td>0.000668</td>                                            |
|      | <td><a href="https://doi.org/10.1039/D0NJ02387F">https://doi.org/10.1039/D0NJ02387F</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co1.5Mn1.5O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>0.016</td>                                               |
|      | <td>0.0000188</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129763">https://doi.org/10.1016/j.snb.2021.129763</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co1.5Mn1.5O4</td>                                        |
|      | <td>peroxidase</td>                                          |
|      | <td>14.46</td>                                               |
|      | <td>0.0000876</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129763">https://doi.org/10.1016/j.snb.2021.129763</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co1.5Mn1.5O4</td>                                        |
|      | <td>oxidase</td>                                             |
|      | <td>0.0029</td>                                              |
|      | <td>0.00001894</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129763">https://doi.org/10.1016/j.snb.2021.129763</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co1.5Mn1.5O4</td>                                        |
|      | <td>laccase</td>                                             |
|      | <td>0.0128</td>                                              |
|      | <td>0.0000792</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129763">https://doi.org/10.1016/j.snb.2021.129763</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Co1.5Mn1.5O4</td>                                        |
|      | <td>catalase</td>                                            |
|      | <td>210</td>                                                 |
|      | <td>0.00264138</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.snb.2021.129763">https://doi.org/10.1016/j.snb.2021.129763</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.055</td>                                               |
|      | <td>0.000467</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.202104247">https://doi.org/10.1002/chem.202104247</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.122</td>                                               |
|      | <td>0.00000151</td>                                          |
|      | <td><a href="https://doi.org/10.1002/chem.202104247">https://doi.org/10.1002/chem.202104247</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.027</td>                                               |
|      | <td>0.000252</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.202104247">https://doi.org/10.1002/chem.202104247</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>0.035</td>                                               |
|      | <td>0.000177</td>                                            |
|      | <td><a href="https://doi.org/10.1002/chem.202104247">https://doi.org/10.1002/chem.202104247</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>V2C</td>                                                 |
|      | <td>oxidase</td>                                             |
|      | <td>0.163</td>                                               |
|      | <td>0.00004075</td>                                          |
|      | <td><a href="https://doi.org/10.1016/j.talanta.2023.124872">https://doi.org/10.1016/j.talanta.2023.124872</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>catalase</td>                                            |
|      | <td>135.1</td>                                               |
|      | <td>0.0059</td>                                              |
|      | <td><a href="https://doi.org/10.1021/acsnano.6b06297">https://doi.org/10.1021/acsnano.6b06297</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pd</td>                                                  |
|      | <td>catalase</td>                                            |
|      | <td>102.4</td>                                               |
|      | <td>0.0022</td>                                              |
|      | <td><a href="https://doi.org/10.1021/acsnano.6b06297">https://doi.org/10.1021/acsnano.6b06297</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>33.84</td>                                               |
|      | <td>0.0000452</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.microc.2021.106238">https://doi.org/10.1016/j.microc.2021.106238</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.952</td>                                               |
|      | <td>0.0000589</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.microc.2021.106238">https://doi.org/10.1016/j.microc.2021.106238</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>38</td>                                                  |
|      | <td>0.0000926</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.microc.2021.106238">https://doi.org/10.1016/j.microc.2021.106238</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ti3C2</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.856</td>                                               |
|      | <td>0.0000804</td>                                           |
|      | <td><a href="https://doi.org/10.1016/j.microc.2021.106238">https://doi.org/10.1016/j.microc.2021.106238</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>17.67</td>                                               |
|      | <td>0.00018</td>                                             |
|      | <td><a href="[https://doi.org/10.1002/anie.201105121 ](https://doi.org/10.1002/anie.201105121)">https://doi.org/10.1002/anie.201105121 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>6.98</td>                                                |
|      | <td>0.00053</td>                                             |
|      | <td><a href="[https://doi.org/10.1002/anie.201105121 ](https://doi.org/10.1002/anie.201105121)">https://doi.org/10.1002/anie.201105121 </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>oxidase</td>                                             |
|      | <td>6.97</td>                                                |
|      | <td>0.00063</td>                                             |
|      | <td><a href="https://doi.org/10.1021/nn102592h">https://doi.org/10.1021/nn102592h</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Pt</td>                                                  |
|      | <td>laccase</td>                                             |
|      | <td>0.12</td>                                                |
|      | <td>0.0001415</td>                                           |
|      | <td><a href="[https://doi.org/10.1007/s10562-017-2106-5    ](https://doi.org/10.1007/s10562-017-2106-5)">https://doi.org/10.1007/s10562-017-2106-5    </a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>AuPt0.178</td>                                           |
|      | <td>catalase</td>                                            |
|      | <td>0.0691</td>                                              |
|      | <td>0.000253</td>                                            |
|      | <td><a href="https://doi.org/10.1007/s12274-015-0904-x">https://doi.org/10.1007/s12274-015-0904-x</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Au</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.0005</td>                                              |
|      | <td>0.00003069</td>                                          |
|      | <td><a href="https://doi.org/10.1007/s00604-021-04942-7">https://doi.org/10.1007/s00604-021-04942-7</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.4113</td>                                              |
|      | <td>0.000134</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3033</td>                                              |
|      | <td>0.000124</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3582</td>                                              |
|      | <td>0.000106</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Fe3O4</td>                                               |
|      | <td>peroxidase</td>                                          |
|      | <td>0.7804</td>                                              |
|      | <td>0.000463</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.9598</td>                                              |
|      | <td>0.0000909</td>                                           |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3912</td>                                              |
|      | <td>0.000314</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.5245</td>                                              |
|      | <td>0.000149</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.827</td>                                               |
|      | <td>0.000305</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>1.0126</td>                                              |
|      | <td>0.000771</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.2432</td>                                              |
|      | <td>0.000675</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.6549</td>                                              |
|      | <td>0.000548</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CoFe</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.3496</td>                                              |
|      | <td>0.00099</td>                                             |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.9147</td>                                              |
|      | <td>0.00088</td>                                             |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.6049</td>                                              |
|      | <td>0.000463</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>1.0328</td>                                              |
|      | <td>0.000707</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>ZnFe2O4</td>                                             |
|      | <td>peroxidase</td>                                          |
|      | <td>0.8139</td>                                              |
|      | <td>0.000542</td>                                            |
|      | <td><a href="https://doi.org/10.1002/smll.202105673">https://doi.org/10.1002/smll.202105673</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>0.163</td>                                               |
|      | <td>0.001331</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsomega.9b03252">https://doi.org/10.1021/acsomega.9b03252</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>CeO2</td>                                                |
|      | <td>peroxidase</td>                                          |
|      | <td>198.34</td>                                              |
|      | <td>0.001515</td>                                            |
|      | <td><a href="https://doi.org/10.1021/acsomega.9b03252">https://doi.org/10.1021/acsomega.9b03252</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>308</td>                                                 |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.0c17579">https://doi.org/10.1021/acsami.0c17579</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | <tr>                                                         |
|      | <td>Ce</td>                                                  |
|      | <td>peroxidase</td>                                          |
|      | <td>0.02</td>                                                |
|      | <td>no</td>                                                  |
|      | <td><a href="https://doi.org/10.1021/acsami.0c17579">https://doi.org/10.1021/acsami.0c17579</a></td> |
|      |                                                              |
|      |                                                              |
|      | </tr>                                                        |
|      |                                                              |
|      | </tbody>                                                     |
|      |                                                              |
|      | </table>                                                     |
|      | <button class="custom-btn btn-8">                            |
|      | <div class="login-signup"><a href="[/database/full](https://dizyme.aicidlab.itmo.ru/database/full)">Full database</a></div> |
|      | </button>                                                    |
|      | </section>                                                   |
|      |                                                              |
|      | <!--  FOOTER  -->                                            |
|      | <section class="footer">                                     |
|      | <div class="col-md-3 align-self-start text-center">          |
|      | <a class="f-logo1" href="https://scamt.ifmo.ru/">            |
|      | <img src="https://scamt.ifmo.ru//images/White logo2.png" alt=""> |
|      | </a>                                                         |
|      | </div>                                                       |
|      |                                                              |
|      | <div class="col-md-3 align-self-end text-center">            |
|      | <a class="f-logo2" href="https://en.itmo.ru/">               |
|      | <img class="itmofoot" src="https://itmo.ru/file/pages/213/logo_osnovnoy_angliyskiy_belyy.png" alt="" |
|      | width="140">                                                 |
|      | </a>                                                         |
|      | </div>                                                       |
|      |                                                              |
|      | <div class="credit">For all technical questions: <span><a href="mailto:razlivina@scamt-itmo.ru">Julia Razlivina</a></span></div> |
|      | <div class="credit">Laboratory head: <span><a href="mailto:vinogradov@scamt-itmo.ru"> Dr. Vladimir Vinogradov</a></span></div> |
|      |                                                              |
|      | </section>                                                   |
|      |                                                              |
|      |                                                              |
|      | <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script> |
|      | <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> |
|      | <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> |
|      | <script src="https://cdn.plot.ly/plotly-2.24.1.min.js" charset="utf-8"></script> |
|      | <script src="https://cdn.datatables.net/1.13.5/js/jquery.dataTables.min.js"></script> |
|      | <script src="[/static/script.js](https://dizyme.aicidlab.itmo.ru/static/script.js)" defer></script> |
|      |                                                              |
|      |                                                              |
|      |                                                              |
|      |                                                              |
|      | <!-- Yandex.Metrika counter -->                              |
|      | <script type="text/javascript" >                             |
|      | (function(m,e,t,r,i,k,a){m[i]=m[i]\|\|function(){(m[i].a=m[i].a\|\|[]).push(arguments)}; |
|      | m[i].l=1*new Date();                                         |
|      | for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }} |
|      | k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}) |
|      | (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym"); |
|      |                                                              |
|      | ym(95452470, "init", {                                       |
|      | clickmap:true,                                               |
|      | trackLinks:true,                                             |
|      | accurateTrackBounce:true,                                    |
|      | webvisor:true                                                |
|      | });                                                          |
|      | </script>                                                    |
|      | <noscript><div><img src="https://mc.yandex.ru/watch/95452470" style="position:absolute; left:-9999px;" alt="" /></div></noscript> |
|      | <!-- /Yandex.Metrika counter -->                             |
|      |                                                              |
|      |                                                              |
|      | </body>                                                      |
|      |                                                              |
|      | </html>                                                      |