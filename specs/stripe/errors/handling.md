# Handling errors

Our Client libraries raise exceptions for many reasons, such as a failed charge, invalid parameters, authentication errors, and network unavailability. We recommend writing code that gracefully handles all possible API exceptions.

- Related guide: [Error Handling](https://docs.stripe.com/error-handling.md)

```sh
# Select a client library to see examples of
# handling different kinds of errors.
```

```ruby
begin
  # Use Stripe's library to make requests...
rescue Stripe::CardError => e
  # A declined card error
  puts "Status: #{e.http_status}"
  puts "Type: #{e.error.type}"
  puts "Code: #{e.error.code}" if e.error.code
  puts "Decline code: #{e.error.decline_code}" if e.error.decline_code
  puts "Param: #{e.error.param}" if e.error.param
  puts "Message: #{e.error.message}"
  puts "Request ID: #{e.request_id}"
rescue Stripe::RateLimitError => e
  # Too many requests made to the API too quickly
  puts "Request ID: #{e.request_id}"
rescue Stripe::InvalidRequestError => e
  # Invalid parameters were supplied to Stripe's API
  puts "Message: #{e.error.message}"
  puts "Param: #{e.error.param}" if e.error.param
  puts "Request ID: #{e.request_id}"
rescue Stripe::AuthenticationError => e
  # Authentication with Stripe's API failed
  puts "Request ID: #{e.request_id}"
rescue Stripe::APIConnectionError => e
  # Network communication with Stripe failed
  puts "Request ID: #{e.request_id}"
rescue Stripe::StripeError => e
  # All other Stripe errors
  puts "Status: #{e.http_status}, Code: #{e.code}, Message: #{e.message}, Request ID: #{e.request_id}"
rescue => e
  # Something else happened, completely unrelated to Stripe
end
```

```sh
# Select a client library to see examples of
# handling different kinds of errors.
```

```python
try:
  # Use Stripe's library to make requests...
  pass
except stripe.error.CardError as e:
  # A declined card error
  print('Status: %s' % e.http_status)
  print('Code: %s' % e.code)
  if e.param:
    print('Param: %s' % e.param)
  print('Message: %s' % e.user_message)
  print('Request ID: %s' % e.request_id)
except stripe.error.RateLimitError as e:
  # Too many requests made to the API too quickly
  print('Request ID: %s' % e.request_id)
except stripe.error.InvalidRequestError as e:
  # Invalid parameters were supplied to Stripe's API
  print('Message: %s' % e.user_message)
  if e.param:
    print('Param: %s' % e.param)
  print('Request ID: %s' % e.request_id)
except stripe.error.AuthenticationError as e:
  # Authentication with Stripe's API failed
  print('Request ID: %s' % e.request_id)
except stripe.error.APIConnectionError as e:
  # Network communication with Stripe failed
  print('Request ID: %s' % e.request_id)
except stripe.error.StripeError as e:
  # All other Stripe errors
  print('Status: %s' % e.http_status)
  print('Code: %s' % e.code)
  print('Message: %s' % e.user_message)
  print('Request ID: %s' % e.request_id)
except Exception as e:
  # Something else happened, completely unrelated to Stripe
  pass
```

```php
try {
  // Use Stripe's library to make requests...
} catch(\Stripe\Exception\CardException $e) {
  // A declined card error
  echo 'Status: ' . $e->getHttpStatus() . '\n';
  echo 'Type: ' . $e->getError()->type . '\n';
  echo 'Code: ' . $e->getError()->code . '\n';
  if ($e->getError()->decline_code) {
    echo 'Decline code: ' . $e->getError()->decline_code . '\n';
  }
  if ($e->getError()->param) {
    echo 'Param: ' . $e->getError()->param . '\n';
  }
  echo 'Message: ' . $e->getError()->message . '\n';
  echo 'Request ID: ' . $e->getRequestId() . '\n';
} catch (\Stripe\Exception\RateLimitException $e) {
  // Too many requests made to the API too quickly
  echo 'Request ID: ' . $e->getRequestId() . '\n';
} catch (\Stripe\Exception\InvalidRequestException $e) {
  // Invalid parameters were supplied to Stripe's API
  echo 'Message: ' . $e->getError()->message . '\n';
  if ($e->getError()->param) {
    echo 'Param: ' . $e->getError()->param . '\n';
  }
  echo 'Request ID: ' . $e->getRequestId() . '\n';
} catch (\Stripe\Exception\AuthenticationException $e) {
  // Authentication with Stripe's API failed
  echo 'Request ID: ' . $e->getRequestId() . '\n';
} catch (\Stripe\Exception\ApiConnectionException $e) {
  // Network communication with Stripe failed
  echo 'Request ID: ' . $e->getRequestId() . '\n';
} catch (\Stripe\Exception\ApiErrorException $e) {
  // All other Stripe API errors
  echo 'Status: ' . $e->getHttpStatus() . '\n';
  echo 'Code: ' . $e->getError()->code . '\n';
  echo 'Message: ' . $e->getError()->message . '\n';
  echo 'Request ID: ' . $e->getRequestId() . '\n';
} catch (Exception $e) {
  // Something else happened, completely unrelated to Stripe
}
```

```java
try {
  // Use Stripe's library to make requests...
} catch (CardException e) {
  // A declined card error
  System.out.println("Status: " + e.getStatusCode());
  System.out.println("Code: " + e.getCode());
  if (e.getDeclineCode() != null) {
    System.out.println("Decline code: " + e.getDeclineCode());
  }
  if (e.getParam() != null) {
    System.out.println("Param: " + e.getParam());
  }
  System.out.println("Message: " + e.getMessage());
  System.out.println("Request ID: " + e.getRequestId());
} catch (RateLimitException e) {
  // Too many requests made to the API too quickly
  System.out.println("Request ID: " + e.getRequestId());
} catch (InvalidRequestException e) {
  // Invalid parameters were supplied to Stripe's API
  System.out.println("Message: " + e.getMessage());
  if (e.getParam() != null) {
    System.out.println("Param: " + e.getParam());
  }
  System.out.println("Request ID: " + e.getRequestId());
} catch (AuthenticationException e) {
  // Authentication with Stripe's API failed
  System.out.println("Request ID: " + e.getRequestId());
} catch (APIConnectionException e) {
  // Network communication with Stripe failed
  System.out.println("Request ID: " + e.getRequestId());
} catch (StripeException e) {
  // All other Stripe errors
  System.out.println("Status: " + e.getStatusCode());
  System.out.println("Code: " + e.getCode());
  System.out.println("Message: " + e.getMessage());
  System.out.println("Request ID: " + e.getRequestId());
} catch (Exception e) {
  // Something else happened, completely unrelated to Stripe
}
```

```javascript
// Note: Node.js API does not throw exceptions, and instead prefers the
// asynchronous style of error handling described below.
//
// An error from the Stripe API or an otherwise asynchronous error
// will be available as the first argument of any Stripe method's callback:
// E.g. stripe.customers.create({...}, function(err, result) {});
//
// Or in the form of a rejected promise.
// E.g. stripe.customers.create({...}).then(
//        function(result) {},
//        function(err) {}
//      );

switch (err.type) {
  case 'StripeCardError':
    // A declined card error
    console.log('Status:', err.statusCode);
    console.log('Code:', err.code);
    if (err.decline_code) console.log('Decline code:', err.decline_code);
    if (err.param) console.log('Param:', err.param);
    console.log('Message:', err.message);
    console.log('Request ID:', err.requestId);
    break;
  case 'StripeRateLimitError':
    // Too many requests made to the API too quickly
    console.log('Request ID:', err.requestId);
    break;
  case 'StripeInvalidRequestError':
    // Invalid parameters were supplied to Stripe's API
    console.log('Message:', err.message);
    if (err.param) console.log('Param:', err.param);
    console.log('Request ID:', err.requestId);
    break;
  case 'StripeAPIError':
    // An error occurred internally with Stripe's API
    console.log('Request ID:', err.requestId);
    break;
  case 'StripeConnectionError':
    // Some kind of error occurred during the HTTPS communication
    console.log('Request ID:', err.requestId);
    break;
  case 'StripeAuthenticationError':
    // You probably used an incorrect API key
    console.log('Request ID:', err.requestId);
    break;
  default:
    if (err instanceof stripe.errors.StripeError) {
      // All other Stripe errors
      console.log('Status: ' + err.statusCode);
      console.log('Code: ' + err.code);
      console.log('Message: ' + err.message);
      console.log('Request ID: ' + err.requestId);
    } else {
      // Handle any other types of unexpected errors
      throw err;
    }
    break;
}
```

```go
_, err := // Go library call

if err != nil {
  // Try to safely cast a generic error to a stripe.Error so that we can get at
  // some additional Stripe-specific information about what went wrong.
  if stripeErr, ok := err.(*stripe.Error); ok {
    // The Code field will contain a basic identifier for the failure.
    switch stripeErr.Code {
      case stripe.ErrorCodeCardDeclined:
      case stripe.ErrorCodeExpiredCard:
      case stripe.ErrorCodeIncorrectCVC:
      case stripe.ErrorCodeIncorrectZip:
      // etc.
    }

    // The Err field can be coerced to a more specific error type with a type
    // assertion. This technique can be used to get more specialized
    // information for certain errors.
    if cardErr, ok := stripeErr.Err.(*stripe.CardError); ok {
      fmt.Printf("Card was declined with code: %v\n", cardErr.DeclineCode)
    } else {
      // All other Stripe API errors
      fmt.Printf("Status: %d, Code: %s, Message: %s, Request ID: %s\n",
        stripeErr.HTTPStatusCode, stripeErr.Code, stripeErr.Msg, stripeErr.RequestID)
    }
  } else {
    // Non-API error (for example, network timeout) — err is a plain Go error, not *stripe.Error
    fmt.Printf("Other error occurred: %v\n", err.Error())
  }
}
```

```dotnet
try {
  // Use Stripe's library to make request
} catch (StripeException e) {
  switch (e.StripeError.Type)
  {
    case "card_error":
      // A declined card error
      Console.WriteLine("Status: " + (int)e.HttpStatusCode);
      Console.WriteLine("Code: " + e.StripeError.Code);
      if (e.StripeError.DeclineCode != null)
        Console.WriteLine("Decline code: " + e.StripeError.DeclineCode);
      if (e.StripeError.Param != null)
        Console.WriteLine("Param: " + e.StripeError.Param);
      Console.WriteLine("Message: " + e.StripeError.Message);
      Console.WriteLine("Request ID: " + e.StripeError.RequestId);
      break;
    case "api_connection_error":
      // Network communication with Stripe failed
      break;
    case "api_error":
      // An error occurred internally with Stripe's API
      break;
    case "authentication_error":
      // Authentication with Stripe's API failed
      break;
    case "invalid_request_error":
      // Invalid parameters were supplied to Stripe's API
      Console.WriteLine("Message: " + e.StripeError.Message);
      if (e.StripeError.Param != null)
        Console.WriteLine("Param: " + e.StripeError.Param);
      break;
    case "rate_limit_error":
      // Too many requests made to the API too quickly
      break;
    case "validation_error":
      break;
    default:
      // All other Stripe errors
      Console.WriteLine("Status: " + (int)e.HttpStatusCode);
      Console.WriteLine("Code: " + e.StripeError?.Code);
      Console.WriteLine("Message: " + e.StripeError?.Message);
      Console.WriteLine("Type: " + e.StripeError?.Type);
      break;
  }
}
```
