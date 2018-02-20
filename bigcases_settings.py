
class settings:
	
    # Scrape settings
    multitask = False                     # Use multiprocessing for scraping RSS?
    multitask_threads = 5
    http_timeout = 30.0	                  # How long to wait for http requests
    file_temp_path = '/pacer'             # Set a temporary path for working with PDFs (i.e., /data/pacer)
    file_archive_path = '/pacer/archive'  # Set a folder to archive downloaded PDFs (i.e., /data/pacer/archive)
    max_files_to_scrape = 10
    
    # Database settings (MySQL server)
    db_host = ''                                      # MySQL host name
    db_user = ''                                      # MySQL username
    db_pass = ''                                      # MySQL password
    db_port = 3306                                    # MySQL port
    db_database = ''                                  # MySQL database
    
    # PACER settings
    pacer_user = ''                                         # PACER username
    pacer_pass = ''                                         # PACER password
    pacer_client = ''                                       # PACER client code
    pacer_max_price = 3.00                                  # Maximum amount to pay for PACER record

    # DocumentCloud credentials
    # dc_user = ''                                            # DocumentCloud username
    # dc_pass = ''                                            # DocumentCloud password
    # dc_project_id = ''                                      # Numeric ID of DocumentCloud project to which to post

    # Twitter credentials
    twitter_app_key = ''                               # Consumer Key (API Key)
    twitter_app_secret = ''                            # Consumer Secret (API Secret)
    twitter_oauth_key = ''                             # Access Token
    twitter_oauth_secret = ''                          # Access Token Secre
	
     # RECAP credentials
     recap_token= ''
