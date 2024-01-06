use std::thread;

#[no_mangle]
pub extern "C" fn fizz_buzz_parallel(start: i32, end: i32) {
    let thread_count = 4; // Aligning with CPU core count
    let mut handles = vec![];
    let chunk_size = (end - start + 1) / thread_count;

    for i in 0..thread_count {
        let thread_start = start + i * chunk_size;
        let thread_end = if i == (thread_count - 1) { end } else { thread_start + chunk_size - 1 };

        let handle = thread::spawn(move || {
            let mut results = Vec::new();
            for num in thread_start..=thread_end {
                let result = match (num % 3, num % 5) {
                    (0, 0) => "FizzBuzz".to_string(),
                    (0, _) => "Fizz".to_string(),
                    (_, 0) => "Buzz".to_string(),
                    _ => num.to_string(),
                };
                results.push(result);
            }
            results
        });

        handles.push(handle);
    }

    for handle in handles {
        let results = handle.join().unwrap();
        // Batched printing or further processing
        for result in results {
            println!("{}", result);
        }
    }
}
